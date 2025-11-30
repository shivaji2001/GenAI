# Stemming is a text preprocessing technique used in Natural Language Processing (NLP) to reduce a word to its root or base form by removing prefixes or suffixes.

# The resulting root word is called a “stem.”
# Stemming is a rule-based and often rough method — the output is not always a valid word.

# | Original Word | Stemmed Word |
# | ------------- | ------------ |
# | Playing       | play         |
# | Studies       | studi        |
# | Runner        | run          |
# | Beautifully   | beauti       |



# Why Stemming is Used?

# To reduce different word forms to one representation.

# Helps improve performance in tasks like:

# Search engines

# Text classification

# Information retrieval

# Topic modeling

# Reduces vocabulary size and simplifies processing.





# Common Stemming Algorithms

# Porter Stemmer (most widely used, aggressive)
# Snowball Stemmer (improved version of Porter)
# Lancaster Stemmer (more aggressive)






# Porter Stemmer (most widely used, aggressive)
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer
words=['running', 'runner', 'ran', 'easily', 'fairly', 'studies', 'studying', 'happiness', 'happily']
stemming=PorterStemmer()
for word in words:
    print(f"PorterStemmer: Original Word:{word} --> Stemmed Word:{stemming.stem(word)}")





# RegexpStemmer Class
# The RegexpStemmer class is a stemming tool in NLTK that uses regular expressions (regex) to remove specific patterns from the end of words.

# What is RegexpStemmer?

# RegexpStemmer is an NLTK stemmer that allows you to define your own custom rule for stemming using a regular expression.
# Instead of relying on predefined algorithms (like Porter or Snowball), you control exactly what gets removed from words.

# Why use RegexpStemmer?

# You want full control over how words are stemmed.

# You want to remove specific endings (like ing, ed, s) based on your needs.

# You want a simpler or domain-specific stemmer.


# Example Usage:
# from nltk.stem import RegexpStemmer

# stemmer = RegexpStemmer('ing$|ed$|s$')

# print(stemmer.stem("playing"))   # play
# print(stemmer.stem("studies"))   # studi
# print(stemmer.stem("liked"))     # lik

from nltk.stem import RegexpStemmer
reg_stemmer=RegexpStemmer('ing$|ed$|s$')
words=['playing', 'studies', 'liked', 'runner', 'happiness']
for word in words:
    print(f"RegexpStemmer: Original Word:{word} --> Stemmed Word:{reg_stemmer.stem(word)}") 





# Snowball Stemmer(improved version of Porter)
from nltk.stem import SnowballStemmer
words=['running', 'runner', 'ran', 'easily', 'fairly', 'studies', 'studying', 'happiness', 'happily']
snow_stemmer=SnowballStemmer('english')
for word in words:
    print(f"SnowballStemmer: Original Word:{word} --> Stemmed Word:{snow_stemmer.stem(word)}")