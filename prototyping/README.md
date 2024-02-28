# Prototyping

This directory is meant as a place to commit code used for data collection, processing and NLP models.

Currently, you can run the following notebooks (in the given order) to get the following outputs:

1. **get_degree_subjects.ipynb**: Creates the [course_programs](./course_programs/) directory, scrapes all the subject pages using the urls in the degree pages located in [test-degrees](./test-degrees/) and saves the HTML in [course_programs](./course_programs/).

2. **clean_subject_pages.ipynb**: Creates the [subject_cleaned](./subjects_cleaned/) directory and transforms the HTML from [course_programs](./course_programs/) to markdown (for website) and place text (for NLP models).

3. **w2v_all_docs.ipynb**: Creates the [word2vec_embeddings](./word2vec_embeddings/) directory, generates the word embeddings for each "subject document" using the Word2Vec Skip-gram model and saves the word-word embedding pair to a JSON file in [word2vec_embeddings/subjects/](./word2vec_embeddings/subjects/).

There are other notebooks in this directory but they are mainly used for testing.
