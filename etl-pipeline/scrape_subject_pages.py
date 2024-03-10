import os

from web_scraping.saveUrlAsHTML import saveUrlAsHTML

from get_university_configs import UniversityConfig

def scrape_subject_pages(university_config: UniversityConfig, subject_codes: set[str]):
    for subject_code in subject_codes:
        uni_path = f"./data/{university_config.abbreviation.lower()}"
        os.makedirs(f"{uni_path}/subjects", exist_ok=True)
        saveUrlAsHTML(
            f"{university_config.subject_options.url_prefix}/{subject_code}.html",
            f"{uni_path}/subjects/{subject_code}.html",
        )
