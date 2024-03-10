import os
import json

from tqdm import tqdm
from bs4 import BeautifulSoup
import html2text
import strip_markdown

from get_university_configs import get_university_configs
from scrape_degree_pages import scrape_degree_pages
from get_subject_codes import get_subject_codes
from utils.await_user_confirmation import await_user_confirmation
from web_scraping.save_url_as_html import save_url_as_html

enable_stepping = False

print("Loading university configurations...")

university_configs = get_university_configs()

print("University configurations loaded successfully!")
print("Number of universities:", len(university_configs), "\n")

if enable_stepping:
    await_user_confirmation()

print("Scraping university degree pages...")

num_pages_scraped = scrape_degree_pages(university_configs)

print("University degree pages saved successfully!")
print("Number of NEW pages scraped:", num_pages_scraped, "\n")

if enable_stepping:
    await_user_confirmation()

print("Getting set of subject codes...")

university_subjects = get_subject_codes(university_configs)

# save relationship between degrees, subjects and universities
if not os.path.exists("./data/uni_degree_subjects_rels.json"):
    with open("./data/uni_degree_subjects_rels.json", "w") as f:
        json.dump(university_subjects.get_degree_to_subjects(), f, indent=2)
else:
    version_num = 2

    while os.path.exists(f"./data/uni_degree_subjects_rels_v{version_num}.json"):
        version_num += 1

    with open(f"./data/uni_degree_subjects_rels_v{version_num}.json", "w") as f:
        json.dump(university_subjects.get_degree_to_subjects(), f, indent=2)

print("Subject codes retrieved successfully!")
print("Number of unique subject codes:", university_subjects.get_num_subjects(), "\n")

if enable_stepping:
    await_user_confirmation()

print("Scraping subject pages...")

num_subject_pages_scraped = 0

for university in university_subjects.get_universities():
    os.makedirs(f"./data/{university}/subjects/html", exist_ok=True)

    for subject_code in tqdm(
        university_subjects.get_subjects(university), desc=university
    ):
        # existing subject codes are retrieved on each iteration to account for new subject codes
        # saved in this process
        existing_subject_codes = set(
            [
                x.replace(".html", "")
                for x in os.listdir(f"./data/{university}/subjects/html")
            ]
        )

        if subject_code not in existing_subject_codes:
            save_url_as_html(
                f"{university_configs[university].subject_options.url_prefix}{subject_code}",
                f"./data/{university}/subjects/html/{subject_code}.html",
            )
            num_subject_pages_scraped += 1

print("Subject pages saved successfully!")
print("Number of NEW subject pages scraped:", num_subject_pages_scraped, "\n")

print("Converting HTML to Markdown and Plain Text...")

for university in university_subjects.get_universities():
    os.makedirs(f"./data/{university}/subjects/markdown", exist_ok=True)
    os.makedirs(f"./data/{university}/subjects/text", exist_ok=True)

    for subject_page in tqdm(
        os.listdir(f"./data/{university}/subjects/html"), desc=university
    ):
        with open(f"./data/{university}/subjects/html/{subject_page}", "r") as f:
            markdown = html2text.html2text(f.read())
            plain_text = strip_markdown.strip_markdown(markdown)

            with open(
                f"./data/{university}/subjects/markdown/{subject_page.replace('.html', '.md')}",
                "w",
            ) as f:
                f.write(markdown)

            with open(
                f"./data/{university}/subjects/text/{subject_page.replace('.html', '.txt')}",
                "w",
            ) as f:
                f.write(plain_text)

print("HTML converted to Markdown and Plain Text successfully!")
