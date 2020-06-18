from . import bag_of_words
from . import term_frequency

_parameterizer_setup = False
_parameterizer = None


def setup_parameterizator(name, articles, force_overwrite=False):
    global _parameterizer_setup, _parameterizer
    if name == "bow":
        bag_of_words.train(articles, force_overwrite)
        _parameterizer_setup = True
        _parameterizer = name
    elif name == "tf":
        term_frequency.train(articles, force_overwrite)
        _parameterizer_setup = True
        _parameterizer = name
    else:
        print("Parameterizer with name'{0}' does not exist".format(name))
        exit(1)


def get_vector_for(article):
    if not _parameterizer_setup:
        print("No parameterizer set up. Make sure to do so first")
        exit(1)

    if _parameterizer == "bow":
        return bag_of_words._get_vector(article)
    elif _parameterizer == "tf":
        return term_frequency._get_vector(article)