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

dataset = pd.read_csv('data/Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

# most frequently used words in a language
nltk.download('stopwords')
# download pos tagging model
nltk.download("averaged_perceptron_tagger")

corpus = []
original_reviews = []

for i in range(0, 1000):
    original_reviews.append(dataset['Review'][i])
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()

    # ================== Text Normalization =====================
    # Stemming is the process of reducing inflection
    # in words to their root forms such as mapping a
    # group of words to the same stem even if the
    # stem itself is not a valid word in the Language.
    # ===================== Inflection ==========================
    # In grammar, inflection is the modification of a word
    # to express different grammatical categories such as
    # tense, case, voice, aspect, person, number, gender,
    # and mood. An inflection expresses one or more grammatical
    # categories with a prefix, suffix or infix, or another
    # internal modification such as a vowel change.

    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

print(f"\nSome Unprocessed Reviews:\n")

for i in range(0, 10):
    print(original_reviews[i])

print(f"\nCorresponding Processed Reviews:\n")

for i in range(0, 10):
    print(corpus[i])

# Creating the Bag of Words model
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# Bigrams
bigrams = ngrams(corpus[:10], 2)
print("\nBigrams\n")
pprint(list(bigrams))
print("\n")

# Trigrams 
trigrams = ngrams(corpus[:10], 3)
print("\nTrigrams\n")
pprint(list(trigrams))
print("\n")

# POS Tagging the first 10 words
print("\nPOS Tagging\n")
pprint(nltk.pos_tag(corpus[:10]))
print("\n")

# TF-IDF Coding!
vectorizer = TfidfVectorizer(stop_words="english")
tf_idf = vectorizer.fit_transform(corpus[:10])
print("Token's used as Features ")
pprint(vectorizer.get_feature_names())
print("\n")
print("Size of the array")
print(tf_idf.shape,"\n")
print("\n")
print("TF-IDF Matrix\n")
print(tf_idf.toarray())
