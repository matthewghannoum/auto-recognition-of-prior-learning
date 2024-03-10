from bs4 import BeautifulSoup

from utils.get_top_level_dirs import get_top_level_dirs
from get_university_configs import UniversityConfig


class UniversitySubjects:
    subjects: dict[str, dict[str, set[str]]]

    def __init__(self):
        self.subjects = {}

    def add_university(self, university_name: str):
        self.subjects[university_name] = {}

    def add_subject(
        self, university_name: str, subject_code: str, degree: str | None = None
    ):
        if degree is not None:
            self.subjects[university_name][subject_code] = set([degree])
        else:
            self.subjects[university_name][subject_code] = set()

    def add_degree(self, university_name: str, subject_code: str, degree: str):
        self.subjects[university_name][subject_code].add(degree)
        
    def get_universities(self):
        return self.subjects.keys()

    def get_subjects(self, university_name: str):
        return self.subjects[university_name]

    def get_num_subjects(self):
        return sum([len(subjects) for subjects in self.subjects.values()])

    def is_subject_in_university(self, university_name: str, subject_code: str):
        return subject_code in self.subjects[university_name]

    def __str__(self):
        return f"UniversitySubjects: {self.subjects}"


def get_subject_codes(university_configs: list[UniversityConfig]):
    university_subjects = UniversitySubjects()

    for uni in get_top_level_dirs("./data"):
        university_subjects.add_university(uni)

        university_config = university_configs[uni]
        urlPrefix = university_config.subject_options.url_prefix

        for degree_code in get_top_level_dirs(f"./data/{uni}"):
            with open(f"./data/{uni}/{degree_code}/{degree_code}.html", "r") as file:
                html = file.read()

            degree_soup = BeautifulSoup(html, "html.parser")

            for subject_link in degree_soup.find_all("a"):
                subject_url = subject_link.get("href")

                if subject_url is None:
                    continue

                subject_code = subject_url.split("/")[-1].replace(".html", "")

                if subject_url.startswith(urlPrefix):
                    if university_subjects.is_subject_in_university(uni, subject_code):
                        university_subjects.add_degree(uni, subject_code, degree_code)
                    else:
                        university_subjects.add_subject(uni, subject_code, degree_code)

    return university_subjects
