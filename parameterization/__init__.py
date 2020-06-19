from preprocessing import body_reader

from . import bag_of_words
from . import term_frequency
from . import tf_idf

_parameterizer_setup = False
_parameterizer = None


def setup_parameterizator(name, articles, force_overwrite=False):
    print("Trying to set up parameterizer")
    global _parameterizer_setup, _parameterizer
    if name == "bow":
        print("Setting up bag of words")
        bag_of_words.train(articles, force_overwrite)
        _parameterizer_setup = True
        _parameterizer = name
    elif name == "tf":
        print("Setting up term frequency")
        term_frequency.train(articles, force_overwrite)
        _parameterizer_setup = True
        _parameterizer = name
    elif name == "tf_idf":
        print("Setting up term frequency - inverse document frequency")
        tf_idf.train(articles, force_overwrite)
        _parameterizer_setup = True
        _parameterizer = name
    else:
        print("Parameterizer with name'{0}' does not exist".format(name))
        exit(1)


def get_vector_for(text):
    if not _parameterizer_setup:
        print("No parameterizer set up. Make sure to do so first")
        exit(1)

    if _parameterizer == "bow":
        return bag_of_words.generate_vector(text)
    elif _parameterizer == "tf":
        return term_frequency.generate_vector(text)
    elif _parameterizer == "tf_idf":
        return tf_idf.generate_vector(text)