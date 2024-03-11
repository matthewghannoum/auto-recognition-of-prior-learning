import os
import json

from utils.await_user_confirmation import await_user_confirmation
from get_university_configs import get_university_configs
from scrape_degree_pages import scrape_degree_pages
from get_subject_codes import get_subject_codes
from scrape_subject_pages import scrape_subject_pages
from convert_html_to_text import convert_html_to_text

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

num_subject_pages_scraped = scrape_subject_pages(
    university_configs, university_subjects
)

print("Subject pages saved successfully!")
print("Number of NEW subject pages scraped:", num_subject_pages_scraped, "\n")

print("Converting HTML to Markdown and Plain Text...")

convert_html_to_text(university_subjects)

print("HTML converted to Markdown and Plain Text successfully!")
