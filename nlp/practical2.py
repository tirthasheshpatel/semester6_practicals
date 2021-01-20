import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

dataset = pd.read_csv('data/Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

# most frequently used words in a language
nltk.download('stopwords')

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

# Creating the Bag of Words model
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

print(f"\nSome Unprocessed Reviews:\n")

for i in range(0, 7):
    print(original_reviews[i])

print(f"\nCorresponding Processed Reviews:\n")

for i in range(0, 7):
    print(corpus[i])
