import os
import json

import weaviate
import weaviate.classes as wvc

from utils.get_top_level_dirs import get_top_level_dirs


def import_into_weaviate():
    client = weaviate.connect_to_custom(
        http_host="localhost",
        http_port=8080,
        http_secure=False,
        grpc_host="localhost",
        grpc_port=50051,
        grpc_secure=False,
        auth_credentials=weaviate.auth.AuthApiKey(
            os.getenv("AUTHENTICATION_APIKEY_ALLOWED_KEYS")
        ),  # Set this environment variable
    )

    for uni in get_top_level_dirs("./data"):
        for embedding_type_dir in get_top_level_dirs(
            f"./data/{uni}/subjects/embeddings"
        ):
            collection_name = f"{uni.upper()}_{embedding_type_dir.upper()}_Subject"

            if collection_name in list(client.collections.list_all().keys()):
                client.collections.delete(collection_name)

            uni_subjects = client.collections.create(
                collection_name,
                vectorizer_config=wvc.config.Configure.Vectorizer.none(),
                vector_index_config=wvc.config.Configure.VectorIndex.hnsw(
                    distance_metric=wvc.config.VectorDistances.COSINE  # select prefered distance metric
                ),
            )

            subject_objs = []

            for subject_embedding_filename in os.listdir(
                f"./data/{uni}/subjects/embeddings/{embedding_type_dir}"
            ):
                if not subject_embedding_filename.endswith(".json"):
                    continue

                with open(
                    f"./data/{uni}/subjects/embeddings/{embedding_type_dir}/{subject_embedding_filename}",
                    "r",
                ) as f:
                    subject_embedding = json.load(f)

                subject_objs.append(
                    wvc.data.DataObject(
                        vector=subject_embedding,
                        properties={
                            "subjectCode": subject_embedding_filename.split(".")[0],
                        },
                    )
                )

            if len(subject_objs) > 0:
                uni_subjects.data.insert_many(subject_objs)

    client.close()  # Close client gracefully
