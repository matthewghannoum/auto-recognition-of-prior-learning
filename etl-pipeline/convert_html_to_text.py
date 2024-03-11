import os

from tqdm import tqdm
import html2text
import strip_markdown

from get_subject_codes import UniversitySubjects


def convert_html_to_text(university_subjects: list[UniversitySubjects]):
    for university in university_subjects.get_universities():
        os.makedirs(f"./data/{university}/subjects/markdown", exist_ok=True)
        os.makedirs(f"./data/{university}/subjects/text", exist_ok=True)

        for subject_page in tqdm(
            os.listdir(f"./data/{university}/subjects/html"), desc=university
        ):
            with open(f"./data/{university}/subjects/html/{subject_page}", "r") as f:
                markdown = html2text.html2text(f.read())
                plain_text = strip_markdown.strip_markdown(markdown)

                with open(
                    f"./data/{university}/subjects/markdown/{subject_page.replace('.html', '.md')}",
                    "w",
                ) as f:
                    f.write(markdown)

                with open(
                    f"./data/{university}/subjects/text/{subject_page.replace('.html', '.txt')}",
                    "w",
                ) as f:
                    f.write(plain_text)
