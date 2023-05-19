import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Read the documents from the CSV file
df = pd.read_csv('Corpus.csv', encoding="ISO-8859-1")

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Generate the TF-IDF matrix for the documents
tfidf_matrix = vectorizer.fit_transform(df['LemaNews'])

background_color = "#f8f8f8"

st.title("Search News of Your Choice")
# Take input query from the user

query = st.text_input("Enter your qurey here", value="")
if st.button('Submit'):
    # Compute the TF-IDF vector for the query
    query_vector = vectorizer.transform([query])

    # Compute the cosine similarity between the query vector and all document vectors
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()

        # Get the indices of the top 10 documents with the highest cosine similarity
    top_doc_indices = cosine_similarities.argsort()[::-1][:10]

        # Display the top 10 documents
    for doc_index in top_doc_indices:
        doc_id = df.loc[doc_index, 'Doc_ID']
        doc_URL = df.loc[doc_index, 'URL']
        doc_Title=df.loc[doc_index, 'LemaTitle']
        print(f"Doc ID: {doc_id}\nText: {doc_URL}\n---")
        st.markdown(f'* <a href="{doc_URL}" style="color: blue; font-size: 15px;">{doc_Title}</a>', unsafe_allow_html=True)






