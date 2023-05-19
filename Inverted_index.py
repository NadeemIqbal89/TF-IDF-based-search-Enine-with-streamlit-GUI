import math
import pandas as pd
import csv



corpus=[]
df = pd.read_csv("Corpus.csv", encoding="ISO-8859-1")
for row in df.itertuples():
    corpus.append(row[5])

# sample corpus
"""corpus = ["The quick brown fox jumps over the lazy dog.",
          "A dog is a man's best friend.",
          "The quick brown fox is a clever animal."]"""

# create a dictionary to store the inverted index
inverted_index = {}
counter=0
# loop through each document in the corpus
for doc_id, doc in enumerate(corpus):
    # tokenize the document by splitting it into words
    words = doc.lower().split()
    # loop through each word in the document
    for word in words:
        # check if the word is already in the inverted index
        if word not in inverted_index:
            # if not, create a new entry for the word
            inverted_index[word] = []
        # add the document id to the posting list for the word
        inverted_index[word].append(doc_id)
# compute the tf-idf for each term in the inverted index
num_docs = len(corpus)
print(num_docs)
for term, posting_list in inverted_index.items():
    posting_list=set(posting_list)
    # compute the document frequency (df) of the term

    df = len(posting_list)
    # compute the inverse document frequency (idf) of the term
    idf = math.log(num_docs / df)
    # loop through each document in the posting list
    
    with open("inverted_index.csv", "a", encoding="ISO-8859-1") as wrtr:
        WR=csv.writer(wrtr)
        WR.writerow([term,len(posting_list), posting_list])
    tf_idf_list = {}
    for doc_id in posting_list:
        # get the term frequency (tf) of the term in the document
        tf = corpus[doc_id].lower().split().count(term)
        # compute the tf-idf score of the term in the document
        tf_idf = tf * idf
        # print the tf-idf score of the term in the document
        print(f"Term: {term}, Doc ID: {doc_id}, TF-IDF: {tf_idf}")
        tf_idf_list[doc_id]=tf_idf
    with open("tf_id.csv", "a", encoding="ISO-8859-1") as wrtr1:
        WR1=csv.writer(wrtr1)
        WR1.writerow([term,tf_idf_list])
