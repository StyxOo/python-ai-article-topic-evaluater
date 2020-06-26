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
    """
    Add two lists by values
    :param a: list a
    :param b: list b
    :return: added list
    """
    new_list = []
    for i in range(len(a)):
        new_list.append(a[i] + b[i])
    return new_list


# Word occurrence
def _generate_word_occurrences(articles):
    """
    Get all word occureces
    :param articles: training articles
    :return:
    """
    global _word_occurrences
    _word_occurrences = []
    bag = bag_of_words.get_vector(articles[0])
    _word_occurrences = bag
    for i in range(1, len(articles)):
        bag = bag_of_words.get_vector(articles[i])
        _word_occurrences = _add_list_values(_word_occurrences, bag)
    with open(_word_occurrences_path, 'w') as json_file:
        json.dump(_word_occurrences, json_file)


def _get_word_occurrences(articles, force_create=False):
    """
    Tries to load word occurrences if not otherwise specified
    :param articles: train article
    :param force_create: force create new word occurreces
    :return:
    """
    global _word_occurrences
    if not force_create:
        if os.path.isfile(_word_occurrences_path):
            with open(_word_occurrences_path) as json_file:
                _word_occurrences = json.load(json_file)
        else:
            _generate_word_occurrences(articles)
    else:
        _generate_word_occurrences(articles)


# IDF
def _generate_idfs(articles, force_create=False):
    """
    Generates idfs. Will load existing is possible
    :param articles: articles for which idfs should be created
    :param force_create: Force creationg of a new vector
    :return:
    """
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
    """
    Tries to get a idfs. Will load existing is possible
    :param articles: articles for which idfs should be created
    :param force_create: Force creationg of a new vector
    :return:
    """
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
    """
    Get path to a tf_idf save location with given id
    :param id: id of article
    :return: path to stored bag
    """
    return os.path.join(os.path.dirname(__file__), './tf_idfs/{0}.json'.format(id))


def _generate_vector(article, save=False):
    """
    Create a new vector and store it
    :param article: article for which to create vector
    :param save: Should vector be saved?
    :return: returns the vector
    """
    tf = term_frequency.get_vector(article)
    vector = generate_vector(article['body'], tf)
    if save:
        if not os.path.isdir(os.path.join(os.path.dirname(__file__), './tf_idfs')):
            os.mkdir(os.path.join(os.path.dirname(__file__), './tf_idfs'))
            print("Created directory to store tf_idfs.")
        with open(_tf_idf_path(article['id']), 'w') as json_file:
            json.dump(vector, json_file)
    return vector


def get_vector(article, force_create=False, save=False):
    """
    Tries to get a vector for an article. Will load existing vector is possible
    :param article: article for which vector should be created
    :param force_create: Force creationg of a new vector
    :param save: Should the vector be saved
    :return: article vector
    """
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
    """
    Generates a vector for a given text
    :param text: text to turn into vector
    :param tf: term frequency for text
    :return: vector for text
    """
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
    """
    Train parameterizer. Makes sure set up is completed. This is required to run before creating vectors
    :param articles: train set
    :param force_create: force creation of new vectors
    :return:
    """
    global _trained
    # Setup
    bag_of_words.train(articles, force_create)
    term_frequency.train(articles, force_create)
    _get_idfs(articles)
    _trained = True
    for article in articles:
        get_vector(article, force_create, True)
