import os

from tqdm import tqdm
from bs4 import BeautifulSoup
import html2text
import strip_markdown

from get_university_configs import get_university_configs
from scrape_degree_pages import scrape_degree_pages
from get_subject_codes import get_subject_codes

print("Loading university configurations...")

university_configs = get_university_configs()

print("University configurations loaded successfully!")
print("Number of universities:", len(university_configs), "\n")

print("Scraping university degree pages...")

num_pages_scraped = scrape_degree_pages(university_configs)

print("University degree pages saved successfully!")
print("Number of NEW pages scraped:", num_pages_scraped, "\n")

print("Getting set of subject codes...")

university_subjects = get_subject_codes(university_configs)

print("Subject codes retrieved successfully!")
print("Number of unique subject codes:", university_subjects.get_num_subjects(), "\n")

print(university_subjects)

exit()
                
# print("Scraping subject pages...")

# for university in tqdm(university_subjects.get_universities()):
#     university_path = f"./data/{university}"
    
#     for subject_code in university_subjects.get_subjects(university):
#         os.makedirs(f"{university_path}/subjects", exist_ok=True)
        
#         if not university_subjects.is_subject_in_university(university, subject_code):
#             continue
        
#         subject_url = university_subjects.get_subjects(university)[subject_code]
#         saveUrlAsHTML(subject_url, f"{university_path}/subjects/{subject_code}.html")

# print("University subject html pages saved successfully!")

# print("Converting HTML to Markdown and Plain text...")

# for (root, dirs, files) in tqdm(os.walk("./data")):
#     if root.endswith("/subjects"):
#         for file in files:
#             if file.endswith(".html"):
#                 filepath = os.path.join(root, file)
#                 with open(filepath, "r") as file:
#                     html = file.read()

#                 soup = BeautifulSoup(html, "html.parser")
#                 markdown_text = html2text.html2text(html)
#                 plain_text = strip_markdown.strip_markdown(markdown_text)

#                 with open(filepath.replace(".html", ".md"), "w") as file:
#                     file.write(markdown_text)

#                 with open(filepath.replace(".html", ".txt"), "w") as file:
#                     file.write(plain_text)
                    
# print("Conversion to Markdown and Plain text successful!")
