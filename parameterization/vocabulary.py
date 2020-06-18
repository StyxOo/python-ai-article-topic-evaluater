import os
import json


_vocabulary_path = os.path.join(os.path.dirname(__file__), './vocabulary.json')
_trained = False
_words = None


def _generate_vocabulary(articles):
    global _words
    _words = []
    for article in articles:
        for word in article['body']:
            if word not in _words:
                _words.append(word)


def get_words():
    if _words is None:
        print("Vocabulary needs to be trained first")
        exit(1)
    return _words


def train(articles, force_create=False):
    global _words
    if not force_create:
        if os.path.isfile(_vocabulary_path):
            with open(_vocabulary_path) as json_file:
                _words = json.load(json_file)
        else:
            _generate_vocabulary(articles)
    else:
        _generate_vocabulary(articles)
