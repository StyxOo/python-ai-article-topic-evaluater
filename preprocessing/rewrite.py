import os
import json
from preprocessing import body_reader


def get_articles():
    if not os.path.isfile('articles.json'):
        print("'articles.json' does not exist. Make sure to run 'sgm_reader.py' first.")
        exit(1)
    with open('articles.json') as json_file:
        return json.load(json_file)


def write_article_dict(dict):
    file_path = os.path.join(os.path.dirname(__file__), './articles_rewritten.json')
    if os.path.isfile(file_path):
        os.remove(file_path)
    with open(file_path, 'w') as json_file:
        json.dump(dict, json_file)


def main():
    articles = get_articles()
    for category in articles:
        for article in articles[category]:
            article['body'] = body_reader.get_words_in(article['body'])
    write_article_dict(articles)


if __name__ == '__main__':
    main()
