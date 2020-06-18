import os
import json

from parameterization import vocabulary

_trained = False


def _bag_path(id):
    return os.path.join(os.path.dirname(__file__), './bags/{0}.json'.format(id))


def _generate_vector(article, save=False):
    if not _trained:
        print("Make sure to train parameterizer first")
        exit(1)

    vector = []
    for word in vocabulary.get_words():
        if word in article['body']:
            vector.append(1)
        else:
            vector.append(0)
    if save:
        if not os.path.isdir(os.path.join(os.path.dirname(__file__), './bags')):
            os.mkdir(os.path.join(os.path.dirname(__file__), './bags'))
            print("Created directory to store bags.")
        with open(_bag_path(article['id']), 'w') as json_file:
            json.dump(vector, json_file)
    return vector


def _get_vector(article, force_create=False, save=False):
    if not force_create:
        if os.path.isfile(_bag_path(article['id'])):
            with open(_bag_path(article['id'])) as json_file:
                vector = json.load(json_file)
        else:
            vector = _generate_vector(article, save)
    else:
        vector = _generate_vector(article, save)

    return vector


def train(articles, force_create=False):
    global _trained
    vocabulary.train(articles, force_create)
    _trained = True
    for article in articles:
        _get_vector(article, force_create, True)
