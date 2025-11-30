# Named Entity Recognition (NER) is an NLP technique used to identify and classify important pieces of information (entities) in text into predefined categories.

# It helps machines understand who, what, where, and when the text is talking about.

# Common Entity Types

# NER typically extracts entities such as:

# Person → (Barack Obama, Elon Musk)

# Organization → (Google, WHO, NASA)

# Location → (India, Paris, New York)

# Date/Time → (2025, Monday, July 3)

# Money → ($50, 100 euros)

# Percent → (80%, 12%)

# Products → (iPhone, Tesla Model S)

# Events → (Olympics, World War II)

# Example

# Sentence:
# "Apple is planning to open a new office in London in 2025."

# NER Output:

# Apple → ORG

# London → GPE (Geo-Political Entity)

# 2025 → DATE






# Why NER is Important

# Extracts meaningful information from text

# Helps in:

# Search engines

# Chatbots

# Information extraction

# Resume screening

# Customer support automation

# Document summarization

# Knowledge graph building






# How NER Works

# NER models use:

# Statistical models

# Machine learning

# Deep learning (like BiLSTM, transformers)

# Pretrained models (spaCy, BERT, etc.)





# sentence="The Eiffel Tower was built from 1887 to 1889 by French engineer Gustave Eiffel, whose company specialized in building metal frameworks and structures."
# """
# Person Eg: Krish C Naik
# Place Or Location Eg: India
# Date Eg: September,24-09-1989
# Time  Eg: 4:30pm
# Money Eg: 1 million dollar
# Organization Eg: iNeuron Private Limited
# Percent Eg: 20%, twenty percent
# """

import nltk

nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
sentence="""The Eiffel Tower is a famous wrought-iron lattice tower in Paris, France, named after engineer Gustave Eiffel, whose company designed and built it between 1887 and 1889. Originally built as the entrance gateway for the 1889 World's Fair, it is now a global icon of French culture and one of the most visited paid attractions in the world"""
words=nltk.word_tokenize(sentence)
tag_elements=nltk.pos_tag(words)

print(nltk.ne_chunk(tag_elements))
nltk.ne_chunk(tag_elements).draw()