import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
from pprint import pprint
import nltk
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from beautify import bcolors

cat_in_the_hat_docs = [
    "One Cent, Two Cents, Old Cent, New Cent: All About Money (Cat in the Hat's Learning Library",
    "Inside Your Outside: All About the Human Body (Cat in the Hat's Learning Library)",
    "Oh, The Things You Can Do That Are Good for You: All About Staying Healthy (Cat in the Hat's Learning Library)",
    "On Beyond Bugs: All About Insects (Cat in the Hat's Learning Library)",
    "There's No Place Like Space: All About Our Solar System (Cat in the Hat's Learning Library)",
]

cv = CountVectorizer(input=cat_in_the_hat_docs)
count_vector = cv.fit_transform(cat_in_the_hat_docs)

# show resulting vocabulary; the numbers are not counts, they are the position in the sparse vector.
print(f"{bcolors.GREEN}" "Vocabulary" f"{bcolors.ENDC}")
pprint(cv.vocabulary_)
print()

# shape of count vector: 5 docs (book titles) and 43 unique words
print(
    f"{bcolors.GREEN}"
    f"Shape of the count vector:"
    f"{bcolors.ENDC}"
    f"{bcolors.CYAN}"
    f" {count_vector.shape[0]} "
    f"{bcolors.ENDC}"
    f"{bcolors.GREEN}"
    f"docs (book titles) and"
    f"{bcolors.ENDC}"
    f"{bcolors.CYAN}"
    f" {count_vector.shape[1]} "
    f"{bcolors.ENDC}"
    f"{bcolors.GREEN}"
    f"unique words.\n"
    f"{bcolors.ENDC}"
)

cv = CountVectorizer(
    input=cat_in_the_hat_docs, stop_words=["all", "in", "the", "is", "and"]
)
count_vector = cv.fit_transform(cat_in_the_hat_docs)

print(
    f"{bcolors.GREEN}"
    f"Shape of the count vector (after filtering selected `stop_words`): "
    f"{bcolors.ENDC}"
    f"{bcolors.CYAN}"
    f" {count_vector.shape[0]} "
    f"{bcolors.ENDC}"
    f"{bcolors.GREEN}"
    f"docs (book titles) and"
    f"{bcolors.ENDC}"
    f"{bcolors.CYAN}"
    f" {count_vector.shape[1]} "
    f"{bcolors.ENDC}"
    f"{bcolors.GREEN}"
    f"unique words."
    f"{bcolors.ENDC}"
)

print(
    f"{bcolors.GREEN}"
    f"Stop words removed in the above example :"
    f"{bcolors.ENDC}"
    f"{bcolors.CYAN}"
    f" {cv.stop_words}"
    f"{bcolors.ENDC}"
)
print()

# ignore terms that appeared in less than 2 documents
cv = CountVectorizer(input=cat_in_the_hat_docs, min_df=2)
count_vector = cv.fit_transform(cat_in_the_hat_docs)

print(f"{bcolors.GREEN}" "Using `min_df = 2`, we have:\n" f"{bcolors.ENDC}")

print(f"{bcolors.CYAN}" "Stop Words\n----------" f"{bcolors.ENDC}")
pprint(cv.stop_words_)
print()
print(f"{bcolors.CYAN}" "Vocabulary\n----------" f"{bcolors.ENDC}")
pprint(cv.vocabulary_)
print()

# ignore terms that appear in 50% of the documents
cv = CountVectorizer(input=cat_in_the_hat_docs, max_df=0.50)
count_vector = cv.fit_transform(cat_in_the_hat_docs)

print(f"{bcolors.GREEN}" "Using `max_df = 0.5`, we have:\n" f"{bcolors.ENDC}")

print(f"{bcolors.CYAN}" "Stop Words\n----------" f"{bcolors.ENDC}")
pprint(cv.stop_words_)
print()
print(f"{bcolors.CYAN}" "Vocabulary\n----------" f"{bcolors.ENDC}")
pprint(cv.vocabulary_)
print()


############################### Custom Tokenizer ##############################


def my_tokenizer(text):
    # create a space between special characters
    text = re.sub("(\\W)", " \\1 ", text)
    # split based on whitespace
    return re.split("\\s+", text)


cv = CountVectorizer(input=cat_in_the_hat_docs, tokenizer=my_tokenizer)
count_vector = cv.fit_transform(cat_in_the_hat_docs)
print(f"{bcolors.GREEN}" "Using custom tokenizer, we have:\n" f"{bcolors.ENDC}")
print(f"{bcolors.CYAN}" "Vocabulary\n----------" f"{bcolors.ENDC}")
pprint(cv.vocabulary_)
print()

###############################################################################


############################### Custom Processing #############################

# init stemmer
porter_stemmer = PorterStemmer()


def my_preprocessor(text):
    text = text.lower()
    text = re.sub("\\W", " ", text)  # remove special chars
    text = re.sub(
        "\\s+(in|the|all|for|and|on)\\s+", " _CONNECTOR_ ", text
    )  # normalize certain words

    # stem words
    words = re.split("\\s+", text)
    stemmed_words = [porter_stemmer.stem(word=word) for word in words]
    return " ".join(stemmed_words)


cv = CountVectorizer(input=cat_in_the_hat_docs, preprocessor=my_preprocessor)
count_vector = cv.fit_transform(cat_in_the_hat_docs)

print(f"{bcolors.GREEN}" "Using custom preprocessor, we have:\n" f"{bcolors.ENDC}")
print(f"{bcolors.CYAN}" "Vocabulary\n----------" f"{bcolors.ENDC}")
pprint(cv.vocabulary_)
print()

###############################################################################
