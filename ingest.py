# loading data and building the search index
# This file handles data loading and index creation - everything we need before we can search

import requests
from minsearch import Index

# use load_faq_data() to fetch the documents
def load_faq_data():
    docs_url = "https://datatalks.club/faq/json/courses.json"
    response = requests.get(docs_url)
    courses_raw = response.json()

    documents = []
    url_prefix = "https://datatalks.club/faq"

    for course in courses_raw:
        course_url = f"""{url_prefix}{course["path"]}"""
        course_response = requests.get(course_url)
        course_response.raise_for_status()
        course_data = course_response.json()

        documents.extend(course_data)

    return documents

# create the minsearch index
def build_index(documents):
    index = Index(
        text_fields=["question", "section", "answer"],
        keyword_fields=["course"]
    )
    # So fit = build the index from the documents.
    index.fit(documents)
    return index

