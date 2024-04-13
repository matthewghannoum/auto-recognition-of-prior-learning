import os
from bs4 import BeautifulSoup

from utils.get_top_level_dirs import get_top_level_dirs
from get_university_configs import UniversityConfig


class UniversitySubjects:
    subjects: dict[str, dict[str, set[str]]]
    subject_to_majors: dict[str, set[str]]

    def __init__(self):
        self.subjects = {}
        self.subject_to_majors = {}

    def add_university(self, university_name: str):
        self.subjects[university_name] = {}
        
    def add_subject_major(self, subject_code: str, major: str | None):
        if subject_code not in self.subject_to_majors:
            self.subject_to_majors[subject_code] = set()

        if major is not None:
            self.subject_to_majors[subject_code].add(major)

    def add_subject(
        self, university_name: str, subject_code: str, degree: str, major: str | None
    ):
        self.add_subject_major(subject_code, major)
            
        if not subject_code in self.subjects[university_name]:
            self.subjects[university_name][subject_code] = set([degree])
        else:
            self.subjects[university_name][subject_code].add(degree)

    def add_degree(self, university_name: str, subject_code: str, degree: str, major: str | None):
        self.add_subject_major(subject_code, major)
        
        self.subjects[university_name][subject_code].add(degree)

    def get_universities(self):
        return list(self.subjects.keys())

    def get_subjects(self, university_name: str):
        return list(self.subjects[university_name].keys())

    def get_subject_to_degrees(self) -> dict[str, str]:
        subject_to_degrees = {}

        for subjects in self.subjects.values():
            for subject, degrees in subjects.items():
                subject_to_degrees[subject] = subject_to_degrees.get(subject, set()).union(degrees)
                
        for subject in subject_to_degrees:
            subject_to_degrees[subject] = list(subject_to_degrees[subject])

        return subject_to_degrees

    def get_num_subjects(self):
        return sum([len(subjects) for subjects in self.subjects.values()])

    def get_num_subjects_per_degree(self):
        num_subject_per_degree = {}

        for university in self.subjects:
            num_subject_per_degree[university] = {}

            for _, degrees in self.subjects[university].items():
                for degree in degrees:
                    if degree not in num_subject_per_degree[university]:
                        num_subject_per_degree[university][degree] = 0

                    num_subject_per_degree[university][degree] += 1

        return num_subject_per_degree
    
    def get_subject_to_majors(self):
        for subject in self.subject_to_majors:
            self.subject_to_majors[subject] = list(self.subject_to_majors[subject])
            
        return self.subject_to_majors

    def is_subject_in_university(self, university_name: str, subject_code: str):
        return subject_code in self.subjects[university_name]

    def __str__(self):
        return f"UniversitySubjects: {self.subjects}"

def get_a_tags(university_config: UniversityConfig, soup: BeautifulSoup):
    container_type = university_config.subject_options.url_criteria.container_type

    if (
        container_type
        is None
    ):
        return soup.find_all("a")

    elements = None
    container_selector = university_config.subject_options.url_criteria.container_selector

    if (
            container_type
            == "tag"
    ):
        elements = soup.find_all(
            container_selector
        )
    else:
        elements = soup.find_all(
            attrs={
                container_type: container_selector
            }
        )

        
    return [element.find("a") for element in elements if element.find("a") is not None]

def get_subject_codes(university_configs: dict[str, UniversityConfig]):
    university_subjects = UniversitySubjects()

    for uni in get_top_level_dirs("./data"):
        university_subjects.add_university(uni)

        university_config = university_configs[uni]

        for degree in university_config.degrees:
            degree_id = degree.name
            degree_path = f"./data/{uni}/degrees/{degree_id}"
            degree_html = f"{degree_path}/{degree_id}.html"

            with open(degree_html, "r") as f:
                soup = BeautifulSoup(f, "html.parser")

                for a in get_a_tags(university_config, soup):
                    subject_url = a.get("href")
                    
                    if subject_url is None:
                        continue
                    
                    if subject_url.startswith(university_config.subject_options.url_criteria.prefix):
                        subject_code = subject_url.split("/")[-1].replace(".html", "")
                        
                        if university_subjects.is_subject_in_university(uni, subject_code):
                            university_subjects.add_degree(uni, subject_code, degree_id, None)
                        else:
                            university_subjects.add_subject(uni, subject_code, degree_id, None)
                            
            for major in degree.majors:
                major_id = major.name
                major_path = f"{degree_path}/{major_id}.html"

                with open(major_path, "r") as f:
                    soup = BeautifulSoup(f, "html.parser")

                    for a in get_a_tags(university_config, soup):                        
                        subject_url = a.get("href")
                        
                        if subject_url is None:
                            continue
                        
                        if subject_url.startswith(university_config.subject_options.url_criteria.prefix):
                            subject_code = subject_url.split("/")[-1].replace(".html", "")
                            
                            if university_subjects.is_subject_in_university(uni, subject_code):
                                university_subjects.add_degree(uni, subject_code, degree_id, major_id)
                            else:
                                university_subjects.add_subject(uni, subject_code, degree_id, major_id)

    return university_subjects
