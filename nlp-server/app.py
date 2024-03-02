import sys
from dotenv import dotenv_values
from flask import Flask
from flask import request, jsonify
import weaviate
import weaviate.classes as wvc
from sentence_transformers import SentenceTransformer

config = dotenv_values(".env")

client = weaviate.connect_to_custom(
    http_host=config["WEAVIATE_HOST"],
    http_port=8080,
    http_secure=False,
    grpc_host=config["WEAVIATE_HOST"],
    grpc_port=50051,
    grpc_secure=False,
    auth_credentials=weaviate.auth.AuthApiKey(
        config["AUTHENTICATION_APIKEY_ALLOWED_KEYS"]
    ),  # Set this environment variable
)

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

subjects = client.collections.get("Subject")

app = Flask(__name__)


@app.get("/search/subject")
def hello():
    query = request.args.get("query")
    print("query:", query, file=sys.stderr)
    query_embedding = model.encode(query, normalize_embeddings=True)

    query_result = subjects.query.near_vector(
        near_vector=query_embedding.tolist(),
        limit=10,
        return_metadata=wvc.query.MetadataQuery(certainty=True),
    )

    response = [
        {"id": x.properties["subjectCode"], "name" : x.properties["name"]}
        for x in query_result.objects
    ]

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)
