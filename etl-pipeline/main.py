import os
import json
import argparse

from dotenv import load_dotenv

from utils.await_user_confirmation import await_user_confirmation
from get_university_configs import get_university_configs
from scrape_degree_pages import scrape_degree_pages
from get_subject_codes import get_subject_codes
from scrape_subject_pages import scrape_subject_pages
from convert_html_to_text import convert_html_to_text
from generate_embeddings import generate_embeddings
from import_into_weaviate import import_into_weaviate

load_dotenv()

is_enable_stepping = (
    os.getenv("IS_ENABLE_STEPPING").lower() == "true"
    if os.getenv("IS_ENABLE_STEPPING") is not None
    else False
)

parser = argparse.ArgumentParser()
parser.add_argument("--enable-stepping", action="store_true", help="require your input for each etl process")
parser.add_argument("--only-generate-embeddings", action="store_true", help="only generate embeddings")
parser.add_argument("--model-type", type=str, help="model type to generate embeddings for", action="append")
parser.add_argument("--only-weaviate-import", action="store_true", help="import embeddings into weaviate")

args = parser.parse_args()

if args.enable_stepping:
    is_enable_stepping = True
    
selected_model_embedding_types = args.model_type

if selected_model_embedding_types is None or len(selected_model_embedding_types) == 0:
    selected_model_embedding_types = ["sbert"]
    
if args.only_generate_embeddings:
    generate_embeddings(selected_model_embedding_types)
    exit(1)
    
if args.only_weaviate_import:
    import_into_weaviate()
    exit(1)

print("Loading university configurations...")

university_configs = get_university_configs()

print("University configurations loaded successfully!")
print("Number of universities:", len(university_configs), "\n")

if is_enable_stepping:
    await_user_confirmation()

print("Scraping university degree pages...")

num_pages_scraped = scrape_degree_pages(university_configs)

print("University degree pages saved successfully!")
print("Number of NEW pages scraped:", num_pages_scraped, "\n")

if is_enable_stepping:
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

num_subjects_per_degree_per_uni = university_subjects.get_num_subjects_per_degree()

for university in university_subjects.get_universities():
    print(
        f"Number of unique subject codes for {university.upper()}:",
        len(university_subjects.get_subjects(university)),
    )
    num_subjects_per_degree = num_subjects_per_degree_per_uni[university]
    
    for degree, num_subjects in num_subjects_per_degree.items():
        print(f"    Number of unique subject codes for {degree}:", num_subjects)

print("Number of unique subject codes:", university_subjects.get_num_subjects(), "\n")

if is_enable_stepping:
    await_user_confirmation()

print("Scraping subject pages...")

num_subject_pages_scraped = scrape_subject_pages(
    university_configs, university_subjects
)

print("Subject pages saved successfully!")
print("Number of NEW subject pages scraped:", num_subject_pages_scraped, "\n")

print("Converting HTML to Markdown and Plain Text...")

convert_html_to_text(university_subjects, university_configs)

print("HTML converted to Markdown and Plain Text successfully!", "\n")

generate_embeddings(selected_model_embedding_types)

print("")

print("Import embeddings into Weaviate...")

import_into_weaviate()

print("Embeddings imported into Weaviate successfully!")
