import nltk
nltk.download('punkt',force=True)
from nltk.tokenize import word_tokenize, sent_tokenize  ,wordpunct_tokenize, TreebankWordTokenizer

corpus='Hi, this is Shivanshu Singh, I am a software engineer. I love coding in Python!. I also enjoy hiking and photography.'

documents=sent_tokenize(corpus)
print(f"documents:{documents}")

type(documents)

for sentence in documents:
    print(f"sentence:{sentence}")

words=word_tokenize(corpus)
print(f"words:{words}")


# will treat punctiuations as separate tokens
word_punct=wordpunct_tokenize(corpus)
print(f"word_punct:{word_punct}")  



tokenizer=TreebankWordTokenizer()
print(f"TreebankWordTokenizer:{tokenizer.tokenize(corpus)}")
