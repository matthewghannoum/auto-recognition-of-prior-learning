import os
import json

from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from InstructorEmbedding import INSTRUCTOR

from typing import Literal
from utils.get_top_level_dirs import get_top_level_dirs

EmbeddingModelNameType = Literal["sbert", "instructor", "word2vec"]


def generate_embeddings(modelTypes: list[EmbeddingModelNameType]):
    for modelType in set(modelTypes):
        print(f"Generating {modelType} embeddings...")

        model = None

        if modelType == "sbert":
            model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
        elif modelType == "instructor":
            model = INSTRUCTOR("hkunlp/instructor-xl")
        else:
            print("Invalid model type. Skipping this model type.")
            continue

        for uni_dir in get_top_level_dirs("./data"):
            uni_subjects_dir = f"./data/{uni_dir}"
            embeddings_dir = f"{uni_subjects_dir}/subjects/embeddings/{modelType}"
            os.makedirs(embeddings_dir, exist_ok=True)

            existing_embeddings = set(os.listdir(embeddings_dir))

            for subject_text_filename in tqdm(
                os.listdir(f"{uni_subjects_dir}/subjects/text"), desc=uni_dir
            ):
                subject_code = subject_text_filename.split(".")[0]
                subject_embedding_filename = f"{subject_code}.json"

                if (
                    os.getenv("IS_REGENERATE_EMBEDDINGS").lower() == "true"
                    or subject_embedding_filename not in existing_embeddings
                ):
                    with open(
                        f"{uni_subjects_dir}/subjects/text/{subject_text_filename}", "r"
                    ) as f:
                        subject_text = f.read()

                    embedding = model.encode([subject_text], normalize_embeddings=True).tolist()[0]

                    with open(
                        f"{embeddings_dir}/{subject_embedding_filename}",
                        "w",
                    ) as f:
                        json.dump(embedding, f)

        print(f"{modelType} embeddings generated successfully!")
