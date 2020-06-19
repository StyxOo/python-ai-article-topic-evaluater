import os
import json

# import parameterization
from parameterization import vocabulary


_trained = False


def _tf_path(id):
    return os.path.join(os.path.dirname(__file__), './vectors/{0}.json'.format(id))


def _generate_vector(article, save=False):
    vector = generate_vector(article['body'])
    if save:
        if not os.path.isdir(os.path.join(os.path.dirname(__file__), './tfs')):
            os.mkdir(os.path.join(os.path.dirname(__file__), './tfs'))
            print("Created directory to store tfs.")
        with open(_tf_path(article['id']), 'w') as json_file:
            json.dump(vector, json_file)
    return vector


def _get_vector(article, force_create=False, save=False):
    if not force_create:
        if os.path.isfile(_tf_path(article['id'])):
            with open(_tf_path(article['id'])) as json_file:
                vector = json.load(json_file)
        else:
            vector = _generate_vector(article, save)
    else:
        vector = _generate_vector(article, save)

    return vector


def generate_vector(text):
    if not _trained:
        print("Make sure to train parameterizer first")
        exit(1)

    frequencies = {}
    for word in text:
        if word in frequencies.keys():
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    vector = []
    for word in vocabulary.get_words():
        try:
            value = frequencies[word]
        except KeyError:
            value = 0
        vector.append(value)
    return vector


def train(articles, force_create=False):
    global _trained
    vocabulary.train(articles, force_create)
    _trained = True
    for article in articles:
        _get_vector(article, force_create, True)