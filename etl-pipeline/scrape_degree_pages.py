import os

from get_university_configs import UniversityConfig
from web_scraping.save_url_as_html import save_url_as_html


def scrape_degree_pages(university_configs: list[UniversityConfig]):
    num_pages_scraped = 0
    
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
                os.makedirs(f"{uni_path}/degrees", exist_ok=True)
                save_url_as_html(
                    degree_url, f"{uni_path}/degrees/{degree_code}.html"
                )
                num_pages_scraped += 1

            continue

        for degree_url in university_config.degree_urls:
            degree_page = degree_url.split("/")[-1]

            if degree_page not in os.listdir(f"{uni_path}/degrees"):
                os.makedirs(f"{uni_path}/degrees", exist_ok=True)
                save_url_as_html(
                    degree_url, f"{uni_path}/degrees/{degree_page}"
                )
                num_pages_scraped += 1
                
    return num_pages_scraped
