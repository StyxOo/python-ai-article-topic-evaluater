import os
import json

# import parameterization
from parameterization import vocabulary


_trained = False
# _dicts = None
# _vectors = None
#
#
# def _dict_path(id):
#     if not os.path.isdir(os.path.join(os.path.dirname(__file__), './dicts')):
#         os.mkdir(os.path.join(os.path.dirname(__file__), './dicts'))
#         print("Created directory to store dictionaries.")
#     return os.path.join(os.path.dirname(__file__), './dicts/{0}.json'.format(id))
#
#
# def _vector_path(id):
#     if not os.path.isdir(os.path.join(os.path.dirname(__file__), './vectors')):
#         os.mkdir(os.path.join(os.path.dirname(__file__), './vectors'))
#         print("Created directory to store vectors.")
#     return os.path.join(os.path.dirname(__file__), './vectors/{0}.json'.format(id))
#
#
# def _save_dicts():
#     for key in _dicts.keys():
#         _save_dict(key)
#
#
# def _save_dict(id):
#     with open(_dict_path(id), 'w') as json_file:
#         json.dump(_dicts[id], json_file)
#
#
# def _save_vectors():
#     for key in _vectors.keys():
#         _save_vector(key)
#
#
# def _save_vector(id):
#     with open(_vector_path(id), 'w') as json_file:
#         json.dump(_vectors[id], json_file)
#
#
# def _load_vectors():
#     files = os.listdir(os.path.join(os.path.dirname(__file__), './vectors'))
#     global _vectors
#     _vectors = {}
#     for file in files:
#         if file.endswith('.json'):
#             id = file.split('.')[0]
#             _vectors[id] = _load_vector(id)
#
#
# def _load_vector(id):
#     if not os.path.isfile(_vector_path(id)):
#         print("Vector for id '{0}' does not exist".format(id))
#         raise FileNotFoundError
#     with open(_vector_path(id)) as json_file:
#         return json.load(json_file)
#
#
# def _generate_frequency_dict(article):
#     frequencies = {}
#     for word in article['body']:
#         if word in frequencies.keys():
#             frequencies[word] += 1
#         else:
#             frequencies[word] = 1
#     return frequencies
#
#
# def _generate_frequency_dicts(articles):
#     global _dicts
#     _dicts = {}
#     for article in articles:
#         _dicts[article['id']] = _generate_frequency_dict(article)
#         _save_dict(article['id'])
#
#
# def _dicts_to_vector():
#     global _vectors
#     _vectors = {}
#     for id, frequency_dict in _dicts.items():
#         values = []
#         for word in parameterization._get_vocabulary():
#             try:
#                 value = frequency_dict[word]
#             except KeyError:
#                 value = 0
#             values.append(value)
#         _vectors[id] = values
#         _save_vector(id)
#
#
# def _generate_vectors(articles):
#     _generate_frequency_dicts(articles)
#     _dicts_to_vector()
#
#
# def get_vectors():
#     if not _trained:
#         print("Make sure to _train parameterizator first")
#         exit(1)
#     if _vectors is None:
#         _load_vectors()
#     return _vectors
#
#
# def get_vector(id):
#     if not _trained:
#         print("Make sure to _train parameterizator first")
#         exit(1)
#     return _load_vector(id)
#
#
# def generate_vector(article):
#     if not _trained:
#         print("Make sure to _train parameterizator first")
#         exit(1)
#     frequency_dict = _generate_frequency_dict()
#     values = []
#     for word in parameterization._get_vocabulary():
#         try:
#             value = frequency_dict[word]
#         except KeyError:
#             value = 0
#         values.append(value)
#     return values


def _tf_path(id):
    return os.path.join(os.path.dirname(__file__), './tf_idfs/{0}.json'.format(id))


def _generate_vector(article, save=False):
    if not _trained:
        print("Make sure to train parameterizer first")
        exit(1)

    frequencies = {}
    for word in article['body']:
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


def train(articles, force_create=False):
    # parameterization._train(articles)
    global _trained
    vocabulary.train(articles, force_create)
    _trained = True
    for article in articles:
        _get_vector(article, force_create, True)

    # if force_create:
    #     print("Forcefully creating new vectors")
    #     _generate_vectors(articles)
    # else:
    #     print("Trying to load existing vectors")
    #     _load_vectors()
    #     if _vectors is None:
    #         print("No existing vectors found. Creating bags")
    #         _generate_vectors(articles)
    #     else:
    #         print("Successfully loaded existing vectors")
    # _initialized = True