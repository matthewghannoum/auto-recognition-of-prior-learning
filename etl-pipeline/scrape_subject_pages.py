import os

from tqdm import tqdm

from get_university_configs import UniversityConfig
from get_subject_codes import UniversitySubjects
from web_scraping.save_url_as_html import save_url_as_html

def scrape_subject_pages(
    university_configs: list[UniversityConfig],
    university_subjects: UniversitySubjects,
):
    num_subject_pages_scraped = 0

    for university in university_subjects.get_universities():
        os.makedirs(f"./data/{university}/subjects/html", exist_ok=True)

        for subject_code in tqdm(
            university_subjects.get_subjects(university), desc=university
        ):
            # existing subject codes are retrieved on each iteration to account for new subject codes
            # saved in this process
            existing_subject_codes = set(
                [
                    x.replace(".html", "")
                    for x in os.listdir(f"./data/{university}/subjects/html")
                ]
            )

            if subject_code not in existing_subject_codes:
                save_url_as_html(
                    f"{university_configs[university].subject_options.url_prefix}{subject_code}",
                    f"./data/{university}/subjects/html/{subject_code}.html",
                )
                num_subject_pages_scraped += 1
                
    return num_subject_pages_scraped
