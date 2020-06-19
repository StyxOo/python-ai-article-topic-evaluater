import os
import json
import math

from parameterization import bag_of_words
from parameterization import term_frequency


_word_occurrences_path = os.path.join(os.path.dirname(__file__), './word_occurrences.json')
_idfs_path = os.path.join(os.path.dirname(__file__), './idfs.json')

_word_occurrences = None
_idfs = None

_trained = False


# Service
def _add_list_values(a, b):
    new_list = []
    for i in range(len(a)):
        new_list.append(a[i] + b[i])
    return new_list


# Word occurrence
def _generate_word_occurrences(articles, force_create=False):
    global _word_occurrences
    _word_occurrences = []
    bag = bag_of_words._get_vector(articles[0])
    _word_occurrences = bag
    for i in range(1, len(articles)):
        bag = bag_of_words._get_vector(articles[i])
        _word_occurrences = _add_list_values(_word_occurrences, bag)
    with open(_word_occurrences_path, 'w') as json_file:
        json.dump(_word_occurrences)


def _get_word_occurrences(articles, force_create=False):
    global _word_occurrences
    if not force_create:
        if os.path.isfile(_word_occurrences_path):
            with open(_word_occurrences_path) as json_file:
                _word_occurrences = json.load(json_file)
        else:
            _generate_word_occurrences(articles, force_create)
    else:
        _generate_word_occurrences(articles, force_create)


# IDF
def _generate_idfs(articles, force_create=False):
    _get_word_occurrences(articles, force_create)
    global _idfs
    _idfs = []
    no_of_articles = len(articles)
    for word_occurrence in _word_occurrences:
        fraction = no_of_articles / word_occurrence
        log = math.log(fraction)
        _idfs.append(log)
    with open(_idfs_path, 'w') as json_file:
        json.dump(_idfs, json_file)


def _get_idfs(articles, force_create=False):
    global _idfs
    if not force_create:
        if os.path.isfile(_idfs_path):
            with open(_idfs_path) as json_file:
                _idfs = json.load(json_file)
        else:
            _generate_idfs(articles, force_create)
    else:
        _generate_idfs(articles, force_create)


# TF-IDF
def _tf_idf_path(id):
    return os.path.join(os.path.dirname(__file__), './tf_idfs/{0}.json'.format(id))


def _generate_vector(article, save=False):
    tf = term_frequency._get_vector(article)
    vector = generate_vector(article['body'], tf)
    if save:
        if not os.path.isdir(os.path.join(os.path.dirname(__file__), './tf_idfs')):
            os.mkdir(os.path.join(os.path.dirname(__file__), './tf_idfs'))
            print("Created directory to store tf_idfs.")
        with open(_tf_idf_path(article[id]), 'w') as json_file:
            json.dump(vector, json_file)
    return vector


def _get_vector(article, force_create=False, save=False):
    if not force_create:
        if os.path.isfile(_tf_idf_path(article['id'])):
            with open(_tf_idf_path(article['id'])) as json_file:
                vector = json.load(json_file)
        else:
            vector = _generate_vector(article, save)
    else:
        vector = _generate_vector(article, save)

    return vector


def generate_vector(text, tf=None):
    if not _trained:
        print("Make sure to train parameterizer first")
        exit(1)
    if tf is None:
        tf = term_frequency.generate_vector(text)
    vector = []
    for i in range(len(tf)):
        vector.append(tf[i] * _idfs[i])
    return vector


def train(articles, force_create=False):
    global _trained
    # Setup
    bag_of_words.train(articles, force_create)
    term_frequency.train(articles, force_create)
    _get_idfs(articles)
    _trained = True
    for article in articles:
        _get_vector(article, force_create, True)
