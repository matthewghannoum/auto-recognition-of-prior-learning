import os
import json

from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from InstructorEmbedding import INSTRUCTOR
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

from typing import Literal
from utils.get_top_level_dirs import get_top_level_dirs

EmbeddingModelNameType = Literal["sbert", "instructor", "word2vec", "doc2vec"]


def generate_doc2vec_embeddings():
    for uni_dir in get_top_level_dirs("./data"):
        uni_subjects_dir = f"./data/{uni_dir}"
        embeddings_dir = f"{uni_subjects_dir}/subjects/embeddings/doc2vec"
        os.makedirs(embeddings_dir, exist_ok=True)

        existing_embeddings = set(
            [name.replace(".json", "") for name in os.listdir(embeddings_dir)]
        )
        document_names = (
            set(
                [
                    name.replace(".txt", "")
                    for name in os.listdir(f"{uni_subjects_dir}/subjects/text")
                ]
            )
            - existing_embeddings
        )

        documents = []

        for document_name in document_names:
            with open(
                f"{uni_subjects_dir}/subjects/text/{document_name}.txt", "r"
            ) as f:
                documents.append(TaggedDocument(f.read().split(), [document_name]))

        # Initialize the Doc2Vec model
        model = Doc2Vec(
            vector_size=50,  # Dimensionality of the document vectors
            window=2,  # Maximum distance between the current and predicted word within a sentence
            min_count=1,  # Ignores all words with total frequency lower than this
            workers=4,  # Number of CPU cores to use for training
            epochs=20,
        )  # Number of training epochs

        # Build the vocabulary
        model.build_vocab(documents)

        # Train the model
        model.train(documents, total_examples=model.corpus_count, epochs=model.epochs)
        
        for document_name in document_names:
            embedding = model.dv[document_name].tolist()

            with open(
                f"{embeddings_dir}/{document_name}.json",
                "w",
            ) as f:
                json.dump(embedding, f)


def generate_transformer_embeddings(model, modelType: Literal["sbert", "instructor"]):
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

                embedding = model.encode(
                    [subject_text], normalize_embeddings=True
                ).tolist()[0]

                with open(
                    f"{embeddings_dir}/{subject_embedding_filename}",
                    "w",
                ) as f:
                    json.dump(embedding, f)


def generate_embeddings(modelTypes: list[EmbeddingModelNameType]):
    for modelType in set(modelTypes):
        print(f"Generating {modelType} embeddings...")

        model = None

        if modelType == "sbert":
            model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
            generate_transformer_embeddings(model, modelType)
        elif modelType == "instructor":
            model = INSTRUCTOR("hkunlp/instructor-xl")
            generate_transformer_embeddings(model, modelType)
        elif modelType == "doc2vec":
            generate_doc2vec_embeddings()
        else:
            print("Invalid model type. Skipping this model type.")
            continue

        print(f"{modelType} embeddings generated successfully!")
