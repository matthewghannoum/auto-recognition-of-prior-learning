import os

from tqdm import tqdm
import html2text
import strip_markdown

from get_university_configs import UniversityConfig, MatchType
from get_subject_codes import UniversitySubjects


def clean_markdown(markdown_text: str, university_config: UniversityConfig) -> str:
    if (
        university_config.subject_options.start_line is None
        or university_config.subject_options.end_line is None
    ):
        return markdown_text

    lines = markdown_text.split("\n")

    start_line_index = None
    end_line_index = None

    start_line, startMatchType = university_config.subject_options.start_line
    end_line, endMatchType = university_config.subject_options.end_line

    def is_line(match_line: str, current_line: str, matchType: MatchType) -> bool:
        if matchType == "equals":
            return current_line == match_line

        if matchType == "contains":
            return match_line in current_line

        if matchType == "startsWith":
            return current_line.startswith(match_line)

        if matchType == "endsWith":
            return current_line.endswith(match_line)

    for i, line in enumerate(lines):
        if is_line(start_line, line, startMatchType):
            start_line_index = i

        if is_line(end_line, line, endMatchType):
            end_line_index = i
            break

    return "\n".join(lines[start_line_index:end_line_index])


def convert_html_to_text(
    university_subjects: list[UniversitySubjects],
    university_configs: dict[str, UniversityConfig],
):
    for university in university_subjects.get_universities():
        os.makedirs(f"./data/{university}/subjects/markdown", exist_ok=True)
        os.makedirs(f"./data/{university}/subjects/text", exist_ok=True)

        for subject_page in tqdm(
            os.listdir(f"./data/{university}/subjects/html"), desc=university
        ):
            with open(f"./data/{university}/subjects/html/{subject_page}", "r") as f:
                markdown = clean_markdown(
                    html2text.html2text(f.read()), university_configs[university]
                )
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
