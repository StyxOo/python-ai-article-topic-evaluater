import os
import json


from bs4 import BeautifulSoup


def find_smg():
    files = []
    for file in os.listdir("reuters"):
        if file.endswith(".sgm"):
            files.append(os.path.join('./reuters', file))
    return files


def read_smg(file):
    f = open(file, 'r')
    data = f.read()
    soup = BeautifulSoup(data, features="html.parser")
    return soup


def get_articles(file):
    soup = read_smg(file)
    articles = soup.find_all('reuters')
    return articles


def get_all_articles(files):
    articles = []
    for file in files:

        articles += get_articles(file)
    return articles


def create_train_test_dict(articles):
    arts = {'train': [], 'test': [], 'unused': []}
    for a in articles:
        if a.attrs['lewissplit'] == 'TRAIN':
            arts['train'].append(a)
        elif a.attrs['lewissplit'] == 'TEST':
            arts['test'].append(a)
        else:
            arts['unused'].append(a)
    return arts


def convert_soups(article_dict):
    new_dict = arts = {'train': [], 'test': [], 'unused': []}
    for a in article_dict['train']:
        new_dict['train'].append(str(a))
    for a in article_dict['test']:
        new_dict['test'].append(str(a))
    for a in article_dict['unused']:
        new_dict['unused'].append(str(a))
    return new_dict


def write_article_dict(dict):
    file_path = os.path.join(os.path.dirname(__file__), './articles.json')
    if os.path.isfile(file_path):
        os.remove(file_path)
    with open(file_path, 'w') as json_file:
        json.dump(dict, json_file)


if __name__ == '__main__':
    files = find_smg()
    articles = get_all_articles(files)
    article_dict = create_train_test_dict(articles)
    article_string_dict = convert_soups(article_dict)
    write_article_dict(article_string_dict)
