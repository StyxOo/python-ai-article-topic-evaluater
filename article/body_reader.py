from . import _nltk
from . import _stopwords
from . import _lemmatizer
from . import _wordnet


import re


def _prepare_text(text):
    text = text.lower()
    text = text.replace('\n', ' ')
    regex = re.compile('[^a-z ]')
    return regex.sub('', text)


def _lemmatize(tagged):
    tag_dict = {"J": _wordnet.ADJ,
                "N": _wordnet.NOUN,
                "V": _wordnet.VERB,
                "R": _wordnet.ADV
                }
    new_tag = tag_dict.get(tagged[1][0], _wordnet.NOUN)
    return _lemmatizer.lemmatize(tagged[0], new_tag)


def get_words(text):
    prepared_text = _prepare_text(text)
    tokens = _nltk.word_tokenize(prepared_text)
    tags = _nltk.pos_tag(tokens)
    lemmatized = [_lemmatize(tag) for tag in tags]
    no_stop = [word for word in lemmatized if word not in _stopwords]
    return no_stop
