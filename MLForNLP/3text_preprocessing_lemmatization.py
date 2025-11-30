# Lemmatization is a text preprocessing technique in NLP that reduces a word to its base or dictionary form, called a lemma, while ensuring the result is a valid English word.

# Unlike stemming, lemmatization considers:

# Word meaning (semantics)

# Part of speech (POS)

# Context

# This makes it more accurate and linguistically correct.



# | Word    | Lemma |
# | ------- | ----- |
# | Studies | study |
# | Better  | good  |
# | Running | run   |
# | Mice    | mouse |


# Why Lemmatization is Used?
# To improve text analysis by reducing words to their base forms.
# Helps in tasks like:
# Information retrieval
# Text classification
# Sentiment analysis
# Question answering
# Reduces vocabulary size while maintaining meaning.
# Common Lemmatization Tools
# WordNetLemmatizer (based on WordNet database)
# SpaCy Lemmatizer (part of SpaCy NLP library)
# TextBlob Lemmatizer (part of TextBlob library)

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet',force=True)


lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize('studies',pos='v'))  # 'study'

words=['running', 'better', 'mice', 'geese', 'fairly', 'happily']
for word in words:
    print(f"Lemmatizer: Original Word:{word} --> Lemma:{lemmatizer.lemmatize(word,pos='v')}")
    