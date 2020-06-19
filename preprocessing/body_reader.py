import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


_lemmatizer = WordNetLemmatizer()
_stopwords = stopwords.words("english")


def _prepare_text(body):
    text = body.lower()
    text = text.replace('\n', ' ')
    regex = re.compile('[^a-z ]')
    return regex.sub('', text)


def _lemmatize(tagged):
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV
                }
    new_tag = tag_dict.get(tagged[1][0], wordnet.NOUN)
    return _lemmatizer.lemmatize(tagged[0], new_tag)


def get_words_in(body):
    prepared_text = _prepare_text(body)
    tokens = nltk.word_tokenize(prepared_text)
    tags = nltk.pos_tag(tokens)
    lemmatized = [_lemmatize(tag) for tag in tags]
    no_stop = [word for word in lemmatized if word not in _stopwords]
    return no_stop
