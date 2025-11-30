# Stopwords are common words in a language that are usually removed during text preprocessing because they do not add significant meaning to the analysis.
# These words occur very frequently but contribute little to the overall understanding of the text.

# Examples of Stopwords

# Some common English stopwords include:
# the, is, am, are, was, were
# in, on, at, of
# for, with, about
# and, or, but
# he, she, they, it


# Why do we remove stopwords?

# To reduce noise in the text
# To focus on meaningful words
# To decrease dataset size
# To improve accuracy and performance of NLP models


# Helps in tasks like:
# Text classification
# Topic modeling
# Search relevance
# Sentiment analysis

# Example

# Sentence:
# "The cat is sleeping on the mat."

# After removing stopwords:
# "cat sleeping mat"

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
nltk.download('stopwords')
nltk.download('punkt_tab')
stemmer=PorterStemmer()

corpus="""I have three visions for India. In 3000 years of our history people from all over the world have come and invaded us, captured our lands, conquered our minds. From Alexander onwards the Greeks, the Turks, the Moguls, the Portuguese, the British, the French, the Dutch, all of them came and looted us, took over what was ours. Yet we have not done this to any other nation. We have not conquered anyone. We have not grabbed their land, their culture and their history and tried to enforce our way of life on them. Why? Because we respect the freedom of others. That is why my FIRST VISION is that of FREEDOM. I believe that India got its first vision of this in 1857, when we started the war of Independence. It is this freedom that we must protect and nurture and build on. If we are not free, no one will respect us.

We have 10 percent growth rate in most areas. Our poverty levels are falling. Our achievements are being globally recognised today. Yet we lack the self-confidence to see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect? MY SECOND VISION for India is DEVELOPMENT. For fifty years we have been a developing nation. It is time we see ourselves as a developed nation. We are among top five nations in the world in terms of GDP.

I have a THIRD VISION. India must stand up to the world. Because I believe that unless India stands up to the world, no one will respect us. Only strength respects strength. We must be strong not only as a military power but also as an economic power. Both must go hand-in-hand. My good fortune was to have worked with three great minds. Dr.Vikram Sarabhai, of the Dept. of Space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material. I was lucky to have worked with all three of them closely and consider this the great opportunity of my life.

I was in Hyderabad giving this lecture, when a 14 year-old girl asked me for my autograph. I asked her what her goal in life is. She replied: I want to live in a developed India. For her, you and I will have to build this developed India. You must proclaim India is not an underdeveloped nation; it is a highly developed nation."""

# print(stopwords.words('english'))
sentences=nltk.sent_tokenize(corpus)
for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    words=[stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i]=' '.join(words)
   
print(sentences)

