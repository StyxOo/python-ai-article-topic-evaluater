import nltk as _nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as _wordnet


_stopwords = stopwords.words("english")
_lemmatizer = WordNetLemmatizer()
