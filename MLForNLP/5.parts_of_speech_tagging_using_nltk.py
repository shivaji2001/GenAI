# POS tags (Part-of-Speech tags) are labels assigned to each word in a sentence to indicate its grammatical role or category.

# This helps NLP models understand the structure and meaning of the sentence.



# What are POS Tags?

# POS tags classify words into categories such as:

# Noun (noun)

# Verb (action/being)

# Adjective (describes a noun)

# Adverb (describes a verb/adjective)

# Pronoun

# Preposition

# Conjunction

# Determiner

# Interjection




# Example

# Sentence:

# "The quick brown fox jumps over the lazy dog."



# POS tagging output:

# The → DET (Determiner)

# quick → ADJ (Adjective)

# brown → ADJ

# fox → NOUN

# jumps → VERB

# over → ADP (Preposition)

# the → DET

# lazy → ADJ

# dog → NOUN




# Why POS Tagging is Used

# Helps understand sentence structure

# Useful for lemmatization (context matters)

# Helps in parsing and grammar analysis

# Important in named entity recognition (NER)

# Supports text classification and sentiment analysis

# Helps disambiguate word meanings (e.g., "book" as noun vs. verb)






from nltk.corpus import stopwords
import nltk
nltk.download('averaged_perceptron_tagger_eng')
corpus="""I have three visions for India. In 3000 years of our history people from all over the world have come and invaded us, captured our lands, conquered our minds. From Alexander onwards the Greeks, the Turks, the Moguls, the Portuguese, the British, the French, the Dutch, all of them came and looted us, took over what was ours. Yet we have not done this to any other nation. We have not conquered anyone. We have not grabbed their land, their culture and their history and tried to enforce our way of life on them. Why? Because we respect the freedom of others. That is why my FIRST VISION is that of FREEDOM. I believe that India got its first vision of this in 1857, when we started the war of Independence. It is this freedom that we must protect and nurture and build on. If we are not free, no one will respect us.

We have 10 percent growth rate in most areas. Our poverty levels are falling. Our achievements are being globally recognised today. Yet we lack the self-confidence to see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect? MY SECOND VISION for India is DEVELOPMENT. For fifty years we have been a developing nation. It is time we see ourselves as a developed nation. We are among top five nations in the world in terms of GDP.

I have a THIRD VISION. India must stand up to the world. Because I believe that unless India stands up to the world, no one will respect us. Only strength respects strength. We must be strong not only as a military power but also as an economic power. Both must go hand-in-hand. My good fortune was to have worked with three great minds. Dr.Vikram Sarabhai, of the Dept. of Space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material. I was lucky to have worked with all three of them closely and consider this the great opportunity of my life.

I was in Hyderabad giving this lecture, when a 14 year-old girl asked me for my autograph. I asked her what her goal in life is. She replied: I want to live in a developed India. For her, you and I will have to build this developed India. You must proclaim India is not an underdeveloped nation; it is a highly developed nation."""


sentences=nltk.sent_tokenize(corpus)
for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    words=[word for word in words if word not in set(stopwords.words('english'))]
    pos_tag=nltk.pos_tag(words)
    print(pos_tag)


for word in "Taj mahal is a beautiful place".split():
    print(nltk.pos_tag([word]))