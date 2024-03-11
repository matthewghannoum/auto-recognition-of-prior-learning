import os
import json

from tqdm import tqdm
from sentence_transformers import SentenceTransformer

from get_university_configs import EmbeddingModelType
from utils.get_top_level_dirs import get_top_level_dirs

sbert_model = SentenceTransformer("paraphrase-MiniLM-L6-v2")


def generate_embeddings(model: EmbeddingModelType):
    print(f"Generating {model} embeddings...")

    if model == "sbert":
        print("Using Sentence-BERT model...")

        for uni_dir in get_top_level_dirs("./data"):
            uni_subjects_dir = f"./data/{uni_dir}"
            embeddings_dir = f"{uni_subjects_dir}/subjects/embeddings/sbert"
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
                    # read subject text file
                    with open(
                        f"{uni_subjects_dir}/subjects/text/{subject_text_filename}", "r"
                    ) as f:
                        subject_text = f.read()

                    embedding = sbert_model.encode([subject_text], normalize_embeddings=True)

                    with open(
                        f"{embeddings_dir}/{subject_embedding_filename}",
                        "w",
                    ) as f:
                        json.dump(embedding.tolist()[0], f)

        print("SBERT Embeddings generated successfully!")
    elif model == "word2vec":
        print("Using Word2Vec model...")
        print("Word2Vec model not implemented yet!")
    else:
        print("Invalid model type!")
