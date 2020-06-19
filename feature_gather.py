import os
import json

import data_generator

import parameterization
import classification

from classification import bayes
from classification import rocchio


def get_train_articles():
    if not os.path.isfile('preprocessing/articles_rewritten.json'):
        print("'articles.json' does not exist. Make sure to run 'sgm_reader.py' first.")
        exit(1)
    with open('preprocessing/articles_rewritten.json') as json_file:
        return json.load(json_file)['train']


def get_topic_of_id(id):
    return train_articles[int(id)]['topics'][0]


if __name__ == '__main__':
    train_articles = get_train_articles()

    parameterization.setup_parameterizator('tf', train_articles)
    topic = rocchio.evaluate(train_articles, train_articles[3])

    # classification.setup_classifier("euclid")
    # closest_id = classification.evaluate(train_articles[1], train_articles)
    # print("Article belongs to '{0}' topic".format(get_topic_of_id(closest_id)))
    # topics = data_generator.get_topic_percent_data(train_articles)
    # words = data_generator.get_word_percent_data(train_articles)
    # words_per_topic = data_generator.get_topic_word_percent_data(train_articles)

    # topic = bayes.evaluate(train_articles, train_articles[32]['body'])
    # topic = bayes.evaluate(train_articles, "money earn product approve")
    print("fin")