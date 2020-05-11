import os
import json
import numpy


def get_train_articles():
    if not os.path.isfile('./articles.json'):
        print("'articles.json' does not exist. Make sure to run 'smg_reader.py' first.")
        exit(1)
    with open('./articles.json') as json_file:
        return json.load(json_file)['train']


def generate_topic_matrix(articles):



if __name__ == '__main__':
    articles = get_train_articles()