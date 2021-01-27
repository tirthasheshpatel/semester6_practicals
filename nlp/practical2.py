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

    # ===========================================================

    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

print(f"\n" f"{bcolors.GREEN}" "Some Unprocessed Reviews" f"{bcolors.ENDC}" "\n")

for i in range(0, 10):
    print(original_reviews[i])

print(f"\n" f"{bcolors.GREEN}" "Corresponding Processed Reviews" f"{bcolors.ENDC}" "\n")

for i in range(0, 10):
    print(corpus[i])

# Creating the Bag of Words model
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# =================== TF-IDF Coding ========================

# TF-IDF Coding! (using first 10 reviews)
print("\n" f"{bcolors.GREEN}" "TF-IDF Coding (using first 10 reviews)" f"{bcolors.ENDC}" "\n")
vectorizer = TfidfVectorizer(stop_words="english")
tf_idf = vectorizer.fit_transform(corpus[:10])
print(f"{bcolors.CYAN}" "Token's used as Features\n" f"{bcolors.ENDC}")
pprint(vectorizer.get_feature_names())
print("\n")
print(f"{bcolors.CYAN}" "Size of the array\n" f"{bcolors.ENDC}")
print(tf_idf.shape,"\n")
print("\n")
print(f"{bcolors.CYAN}" "TF-IDF Matrix\n" f"{bcolors.ENDC}")
print(tf_idf.toarray())

# ==========================================================

# Sentence used in the models below
words = ["I", "am", "a", "student", "at", "nirma", "university"]

# =====================  N-Gram Models =====================

# Unigrams
bigrams = ngrams(words, 1)
print("\n" f"{bcolors.GREEN}" "Unigrams" f"{bcolors.ENDC}" "\n")
pprint(list(bigrams))
print("\n")

# Bigrams
bigrams = ngrams(words, 2)
print("\n" f"{bcolors.GREEN}" "Bigrams" f"{bcolors.ENDC}" "\n")
pprint(list(bigrams))
print("\n")

# Trigrams
trigrams = ngrams(words, 3)
print("\n" f"{bcolors.GREEN}" "Trigrams" f"{bcolors.ENDC}" "\n")
pprint(list(trigrams))
print("\n")

# ==========================================================

# =================== POS Tagging ==========================

# Tagging is a kind of classification that may be defined
# as the automatic assignment of description to the tokens.
# Here the descriptor is called tag, which may represent
# one of the part-of-speech, semantic information and so on.

# Now, if we talk about Part-of-Speech (PoS) tagging,
# then it may be defined as the process of assigning
# one of the parts of speech to the given word. It is
# generally called POS tagging. In simple words, we
# can say that POS tagging is a task of labelling each
# word in a sentence with its appropriate part of speech.
# We already know that parts of speech include nouns,
# verb, adverbs, adjectives, pronouns, conjunction and
# their sub-categories.

# In NLTK, the abbreviation for "adjective" is "JJ".

# The NLTK tagger marks "singular nouns" ("NN") with different
# tags than "plural nouns" ("NNS").

# POS Tagging the first 10 words
print("\n" f"{bcolors.GREEN}" "POS Tagging" f"{bcolors.ENDC}" "\n")
pprint(nltk.pos_tag(words))
print("\n")

# ==========================================================
