import os
from dataclasses import dataclass
from typing import Literal

import yaml

from generate_embeddings import EmbeddingModelNameType

match_type = Literal["equals", "contains", "startsWith", "endsWith"]


@dataclass
class SubjectOptions:
    url_prefix: str
    start_line: tuple[str, match_type]
    end_line: tuple[str, match_type]


@dataclass
class UniversityConfig:
    name: str
    abbreviation: str
    degree_urls: list[str]
    subject_options: SubjectOptions
    embedding_method: EmbeddingModelNameType


def get_university_configs():
    university_configs: dict[str, UniversityConfig] = {}

    for filename in os.listdir("./configs/"):
        if filename.endswith(".yml") or filename.endswith(".yaml"):
            with open(f"./configs/{filename}", "r") as file:
                university_config = yaml.safe_load(file)["university"]

                subjectOptions = university_config["subject_options"]
                subjectOptions = SubjectOptions(
                    subjectOptions["url_prefix"],
                    (
                        subjectOptions["start_line"]["value"],
                        subjectOptions["start_line"]["match_type"],
                    ),
                    (
                        subjectOptions["end_line"]["value"],
                        subjectOptions["end_line"]["match_type"],
                    ),
                )

                university_configs[university_config["abbreviation"]] = (
                    UniversityConfig(
                        university_config["name"],
                        university_config["abbreviation"],
                        university_config["degree_urls"],
                        subjectOptions,
                        university_config["embedding_method"],
                    )
                )

    return university_configs
