import os
from dataclasses import dataclass
from typing import Literal

import yaml

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


def get_university_configs():
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

                university_configs[university_config["abbreviation"]] = (
                    UniversityConfig(
                        university_config["name"],
                        university_config["abbreviation"],
                        university_config["degreeUrls"],
                        subjectOptions,
                        university_config["embeddingMethod"],
                    )
                )

    return university_configs
