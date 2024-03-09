import os
from dataclasses import dataclass
from typing import Literal

import yaml
from bs4 import BeautifulSoup

from web_scraping import saveUrlAsHTML

MatchType = Literal["equals", "contains", "startsWith", "endsWith"]
EmbeddingModelType = Literal["sbert", "word2vec"]


@dataclass
class SubjectOptions:
    url_prefix: str
    start_line: tuple[str, MatchType]
    end_line: tuple[str, MatchType]


@dataclass
class UniversityConfig:
    name: str
    abbreviation: str
    degree_urls: list[str]
    subject_options: SubjectOptions
    embedding_method: EmbeddingModelType


university_configs: dict[str, UniversityConfig] = {}

for filename in os.listdir("./configs/"):
    if filename.endswith(".yml") or filename.endswith(".yaml"):
        with open(f"./configs/{filename}", "r") as file:
            university_config = yaml.safe_load(file)["university"]

            subjectOptions = university_config["subjectOptions"]
            subjectOptions = SubjectOptions(
                subjectOptions["urlPrefix"],
                (
                    subjectOptions["startLine"]["value"],
                    subjectOptions["startLine"]["matchType"],
                ),
                (
                    subjectOptions["endLine"]["value"],
                    subjectOptions["endLine"]["matchType"],
                ),
            )

            university_configs[university_config["abbreviation"]] = UniversityConfig(
                university_config["name"],
                university_config["abbreviation"],
                university_config["degreeUrls"],
                subjectOptions,
                university_config["embeddingMethod"],
            )

print("University configurations loaded successfully!")
print("Number of universities:", len(university_configs))

# scrapes degree pages
for university_config in university_configs.values():
    uni_dirs = [
        name
        for name in os.listdir("./data")
        if os.path.isdir(os.path.join("./data", name))
    ]

    abbreviation = university_config.abbreviation.lower()
    uni_path = f"./data/{abbreviation}"

    if abbreviation not in uni_dirs:
        for degree_url in university_config.degree_urls:
            degree_code = degree_url.split("/")[-1].replace(".html", "")
            os.makedirs(f"{uni_path}/{degree_code}", exist_ok=True)
            saveUrlAsHTML(degree_url, f"{uni_path}/{degree_code}/{degree_code}.html")

        continue

    for degree_url in university_config.degree_urls:
        degree_code = degree_url.split("/")[-1].replace(".html", "")

        if degree_code not in os.listdir(uni_path):
            degree_code = degree_url.split("/")[-1].replace(".html", "")
            os.makedirs(f"{uni_path}/{degree_code}", exist_ok=True)
            saveUrlAsHTML(degree_url, f"{uni_path}/{degree_code}/{degree_code}.html")

print("University degree pages saved successfully!")

for filename in os.listdir("./data"):
    if not os.path.isdir(os.path.join("./data", filename)):
        continue

    uni = filename

    university_config = university_configs[uni]
    urlPrefix = university_config.subject_options.url_prefix

    for degree_code in os.listdir(f"./data/{uni}"):
        degree_path = f"./data/{uni}/{degree_code}"
        degree_subjects_path = f"{degree_path}/subjects"

        os.makedirs(degree_subjects_path, exist_ok=True)
        subject_codes = set(
            [
                name
                for name in os.listdir(f"{degree_subjects_path}")
                if os.path.isdir(os.path.join(f"{degree_subjects_path}", name))
            ]
        )

        with open(f"{degree_path}/{degree_code}.html", "r") as file:
            html = file.read()

        degree_soup = BeautifulSoup(html, "html.parser")

        for subject_link in degree_soup.find_all("a"):
            subject_url = subject_link.get("href")

            if subject_url is None:
                continue

            subject_code = subject_url.split("/")[-1].replace(".html", "")

            if subject_code in subject_codes or not subject_url.startswith(urlPrefix):
                continue

            if subject_code not in subject_codes:
                os.makedirs(f"{degree_subjects_path}/{subject_code}", exist_ok=True)
                saveUrlAsHTML(
                    subject_url,
                    f"{degree_subjects_path}/{subject_code}/{subject_code}.html",
                )

        break

print("University subject html pages saved successfully!")
