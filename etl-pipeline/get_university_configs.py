import os
from dataclasses import dataclass
from typing import Literal

import yaml

from generate_embeddings import EmbeddingModelNameType

MatchType = Literal["equals", "contains", "startsWith", "endsWith"]


@dataclass
class UrlCriteria:
    prefix: str
    container_type: str | None
    container_selector: str | None


@dataclass
class SubjectOptions:
    url_criteria: UrlCriteria
    start_line: tuple[str, MatchType]
    end_line: tuple[str, MatchType]


@dataclass
class Major:
    name: str
    url: str


class Degree:
    name: str
    code: str | None
    url: str
    majors: list[Major]

    def __init__(self, name: str, url: str, code: str | None = None):
        self.name = name
        self.code = code
        self.url = url
        self.majors = []

    def add_major(self, major: Major):
        self.majors.append(major)


@dataclass
class UniversityConfig:
    name: str
    abbreviation: str
    degrees: list[Degree]
    subject_options: SubjectOptions


def get_university_configs():
    university_configs: dict[str, UniversityConfig] = {}

    for filename in os.listdir("./configs/"):
        if filename.endswith(".yml") or filename.endswith(".yaml"):
            with open(f"./configs/{filename}", "r") as file:
                university_config = yaml.safe_load(file)["university"]

                subjectOptions = university_config["subject_options"]
                subjectOptions = SubjectOptions(
                    UrlCriteria(
                        subjectOptions["url_criteria"]["prefix"],
                        subjectOptions["url_criteria"].get("container_type", None),
                        subjectOptions["url_criteria"].get("container_selector", None),
                    ),
                    (
                        subjectOptions["start_line"]["value"],
                        subjectOptions["start_line"]["match_type"],
                    ),
                    (
                        subjectOptions["end_line"]["value"],
                        subjectOptions["end_line"]["match_type"],
                    ),
                )

                degrees = []

                for degree_config in university_config["degrees"]:
                    degree = Degree(
                        degree_config["name"], degree_config["url"], degree_config.get("code", None)
                    )

                    for major in degree_config.get("majors", []):
                        degree.add_major(Major(major["name"], major["url"]))

                    degrees.append(degree)

                university_configs[university_config["abbreviation"]] = (
                    UniversityConfig(
                        university_config["name"],
                        university_config["abbreviation"],
                        degrees,
                        subjectOptions,
                    )
                )

    return university_configs
