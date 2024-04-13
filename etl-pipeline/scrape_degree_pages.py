import os

from get_university_configs import UniversityConfig
from web_scraping.save_url_as_html import save_url_as_html


def scrape_degree_pages(university_configs: dict[str, UniversityConfig]):
    num_pages_scraped = 0

    for university_config in university_configs.values():
        uni_dirs = [
            name
            for name in os.listdir("./data")
            if os.path.isdir(os.path.join("./data", name))
        ]

        abbreviation = university_config.abbreviation.lower()
        uni_path = f"./data/{abbreviation}"
        os.makedirs(f"{uni_path}/degrees", exist_ok=True)

        # if university directory does not exist, create it
        # and scrape all degree pages for that university
        if abbreviation not in uni_dirs:
            for degree in university_config.degrees:
                degree_id = degree.name
                os.makedirs(f"{uni_path}/degrees/{degree_id}", exist_ok=True)
                save_url_as_html(degree.url, f"{uni_path}/degrees/{degree_id}/{degree_id}.html")
                num_pages_scraped += 1
                
                for major in degree.majors:
                    major_id = major.name
                    save_url_as_html(major.url, f"{uni_path}/degrees/{degree_id}/{major_id}.html")
                    num_pages_scraped += 1
            continue

        # if university directory exists, check if degree pages exist
        for degree in university_config.degrees:
            degree_id = degree.name
            
            if degree_id not in os.listdir(f"{uni_path}/degrees"):
                os.makedirs(f"{uni_path}/degrees/{degree_id}", exist_ok=True)
                save_url_as_html(degree.url, f"{uni_path}/degrees/{degree_id}/{degree_id}.html")
                num_pages_scraped += 1
            
            for major in degree.majors:
                major_id = major.name
                if f"{major_id}.html" not in os.listdir(f"{uni_path}/degrees/{degree_id}"):
                    save_url_as_html(major.url, f"{uni_path}/degrees/{degree_id}/{major_id}.html")
                    num_pages_scraped += 1

    return num_pages_scraped
