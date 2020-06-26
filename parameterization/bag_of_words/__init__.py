import os
import json

from parameterization import vocabulary

_trained = False


def _bag_path(id):
    """
    Get path to a bags save location with given id
    :param id: id of article
    :return: path to stored bag
    """
    return os.path.join(os.path.dirname(__file__), './bags/{0}.json'.format(id))


def _generate_vector(article, save=False):
    """
    Create a new vector and store it
    :param article: article for which to create vector
    :param save: Should vector be saved?
    :return: returns the vector
    """
    vector = generate_vector(article['body'])
    if save:
        if not os.path.isdir(os.path.join(os.path.dirname(__file__), './bags')):
            os.mkdir(os.path.join(os.path.dirname(__file__), './bags'))
            print("Created directory to store bags.")
        with open(_bag_path(article['id']), 'w') as json_file:
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
        if os.path.isfile(_bag_path(article['id'])):
            with open(_bag_path(article['id'])) as json_file:
                vector = json.load(json_file)
        else:
            vector = _generate_vector(article, save)
    else:
        vector = _generate_vector(article, save)

    return vector


def generate_vector(text):
    """
    Generates a vector for a given text
    :param text: text to turn into vector
    :return: vector for text
    """
    if not _trained:
        print("Make sure to train parameterizer first")
        exit(1)

    vector = []
    for word in vocabulary.get_words():
        if word in text:
            vector.append(1)
        else:
            vector.append(0)
    return vector


def train(articles, force_create=False):
    """
    Train parameterizer. Makes sure set up is completed. This is required to run before creating vectors
    :param articles: train set
    :param force_create: force creation of new vectors
    :return:
    """
    global _trained
    vocabulary.train(articles, force_create)
    _trained = True
    for article in articles:
        get_vector(article, force_create, True)
