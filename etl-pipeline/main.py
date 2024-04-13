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

parser = argparse.ArgumentParser()
parser.add_argument(
    "--disable-stepping",
    action="store_true",
    help="do not require your input for each etl process",
)
parser.add_argument(
    "--only-generate-embeddings", action="store_true", help="only generate embeddings"
)
parser.add_argument(
    "--regenerate-existing-embeddings",
    action="store_true",
    help="regenerate existing embeddings",
)
parser.add_argument(
    "--model-type",
    type=str,
    help="model type to generate embeddings for",
    action="append",
)
parser.add_argument(
    "--only-weaviate-import",
    action="store_true",
    help="import embeddings into weaviate",
)
parser.add_argument(
    "--prune-subjects",
    action="store_true",
    help="remove subject files if it is not in subject codes in degree pages",
)

args = parser.parse_args()

is_enable_stepping = not args.disable_stepping
is_regenerate_embeddings = args.regenerate_existing_embeddings
is_prune_subjects = args.prune_subjects

selected_model_embedding_types = args.model_type

if (
    selected_model_embedding_types is None
    or len(selected_model_embedding_types) == 0
    or selected_model_embedding_types[0] == "all"
):
    selected_model_embedding_types = [
        "sbert",
        "instructor",
        "mxbai",
        "doc2vec",
        "glove",
    ]

if selected_model_embedding_types[0] == "all":
    generate_embeddings(selected_model_embedding_types, is_regenerate_embeddings)
    exit(1)

if args.only_generate_embeddings:
    generate_embeddings(selected_model_embedding_types, is_regenerate_embeddings)
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
subject_to_majors = university_subjects.get_subject_to_majors()

# save relationship between degrees, subjects and universities
with open("./data/subject_to_degrees.json", "w") as f:
    json.dump(university_subjects.get_subject_to_degrees(), f, indent=2)
    
# save relationship between subjects and majors
with open("./data/subject_to_majors.json", "w") as f:
    json.dump(subject_to_majors, f, indent=2)

print("Subject codes retrieved successfully!")

if is_prune_subjects:
    print("")
    print("Pruning subject files...")

    num_pruned_files = {}

    for university in university_subjects.get_universities():
        subjects = set(university_subjects.get_subjects(university))

        for file_type, file_ext in [
            ["html", "html"],
            ["text", "txt"],
            ["markdown", "md"],
            ["embeddings", "json"],
        ]:
            files = os.listdir(f"./data/{university}/subjects/{file_type}")

            if file_type == "embeddings":
                for embedding_type in files:
                    for embedding_file in os.listdir(
                        f"./data/{university}/subjects/{file_type}/{embedding_type}"
                    ):
                        if embedding_file.replace(f".{file_ext}", "") not in subjects:
                            os.remove(
                                f"./data/{university}/subjects/{file_type}/{embedding_type}/{embedding_file}"
                            )
                            num_pruned_files[file_type] = (
                                num_pruned_files.get(file_type, 0) + 1
                            )

                continue

            for subject in files:
                if subject.replace(f".{file_ext}", "") not in subjects:
                    os.remove(f"./data/{university}/subjects/{file_type}/{subject}")
                    num_pruned_files[file_type] = num_pruned_files.get(file_type, 0) + 1

    print("Number of html files pruned:", num_pruned_files.get("html", 0))
    print("Number of text files pruned:", num_pruned_files.get("text", 0))
    print("Number of markdown files pruned:", num_pruned_files.get("markdown", 0))
    print("Number of embeddings files pruned:", num_pruned_files.get("embeddings", 0))
    print("Subject files pruned successfully!", "\n")

num_subjects_per_degree_per_uni = university_subjects.get_num_subjects_per_degree()

total_new_subjects = 0

for university in university_subjects.get_universities():
    subjects = university_subjects.get_subjects(university)
    scraped_subjects = os.listdir(f"./data/{university}/subjects/html")

    print(
        f"Number of unique subject codes for {university.upper()}:",
        len(subjects),
    )
    num_new_subjects = len(
        set([f"{id}.html" for id in subjects]) - set(scraped_subjects)
    )
    total_new_subjects += num_new_subjects
    print(f"Number of NEW subject codes for {university.upper()}: {num_new_subjects}")

    num_subjects_per_degree = num_subjects_per_degree_per_uni[university]

    for degree, num_subjects in num_subjects_per_degree.items():
        print(f"    Number of unique subject codes for {degree}:", num_subjects)

print("Number of unique subject codes:", university_subjects.get_num_subjects())
print("Number of NEW subject codes:", total_new_subjects, "\n")

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

generate_embeddings(selected_model_embedding_types, is_regenerate_embeddings)

print("")

print("Import embeddings into Weaviate...")

import_into_weaviate()

print("Embeddings imported into Weaviate successfully!")
