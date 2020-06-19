import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


_lemmatizer = WordNetLemmatizer()
_stopwords = stopwords.words("english")


def _prepare_text(body):
    """
    Prepares text for stemming and lammentization
    :param body: text to prepare
    :return: prepared text
    """
    text = body.lower()
    text = text.replace('\n', ' ')
    regex = re.compile('[^a-z ]')
    return regex.sub('', text)


def _lemmatize(tagged):
    """
    Lemmatize tagged text
    :param tagged: tagged text
    :return: lemmatized text
    """
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV
                }
    new_tag = tag_dict.get(tagged[1][0], wordnet.NOUN)
    return _lemmatizer.lemmatize(tagged[0], new_tag)


def get_words_in(body):
    """
    Get lemmatized and stemmed words without stopwords in text
    :param body: text to work with
    :return: cleaned text
    """
    prepared_text = _prepare_text(body)
    tokens = nltk.word_tokenize(prepared_text)
    tags = nltk.pos_tag(tokens)
    lemmatized = [_lemmatize(tag) for tag in tags]
    no_stop = [word for word in lemmatized if word not in _stopwords]
    return no_stop
