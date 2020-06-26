from preprocessing import body_reader

from . import euclidean
from . import bayes
from . import rocchio


_trained = False
_classifier = None


def setup_classifier(name):
    """
    Sets up a classifier for use
    :param name: name of classifier. Choices are: euclid, bayes and rocchio
    :return:
    """
    global _classifier, _trained
    if name == "euclid":
        _classifier = name
        _trained = True
    elif name == "bayes":
        _classifier = name
        _trained = True
    elif name == "rocchio":
        _classifier = name
        _trained = True
    else:
        print("Classifier with name '{0} does not exist".format(name))
        raise Exception


def evaluate(text, articles, no_preprocess=False):
    """
    Evaluate a text with given train set using the set up classifier
    :param text: text to evaluate
    :param articles: train articles
    :return: topic
    """
    if not _trained:
        print("No classifier initialized. Make sure to do so first")
        raise Exception

    if not no_preprocess:
        text = body_reader.get_words_in(text)

    if _classifier == "euclid":
        return euclidean.evaluate(articles, text)
    elif _classifier == "bayes":
        return bayes.evaluate(articles, text)
    elif _classifier == "rocchio":
        return rocchio.evaluate(articles, text)
