import os
import json


from bs4 import BeautifulSoup


def find_smg():
    """
    finds all sgm files
    :return: sgm files
    """
    files = []
    for file in os.listdir("reuters"):
        if file.endswith(".sgm"):
            files.append(os.path.join('./reuters', file))
    return files


def read_smg(file):
    """
    Convert sgm file to beautiful soup
    :param file: sgm file
    :return: soup
    """
    f = open(file, 'r')
    data = f.read()
    soup = BeautifulSoup(data, features="html.parser")
    return soup


def get_articles(file):
    """
    Gets all articles in a sgm file
    :param file: sgm file
    :return: articles
    """
    soup = read_smg(file)
    articles = soup.find_all('reuters')
    return articles


def get_all_articles(files):
    """
    Gets all articles in all files
    :param files: all sgm files
    :return: articles
    """
    articles = []
    for file in files:
        articles += get_articles(file)
    return articles


def create_train_test_dict(articles):
    """
    Categorize articles into train, test and unused
    :param articles: articles
    :return: article dictionary
    """
    arts = {'train': [], 'test': [], 'unused': []}
    for a in articles:
        info = read_article_info(a)
        if info is not None:
            if a.attrs['lewissplit'] == 'TRAIN':
                if len(info['topics']) > 0:
                    arts['train'].append(info)
                else:
                    arts['test'].append(info)
            elif a.attrs['lewissplit'] == 'TEST':
                arts['test'].append(info)
            else:
                arts['unused'].append(info)
    return arts


def get_topics(soup):
    """
    Get all topics for article
    :param soup: rticle soup
    :return: topics
    """
    topic_tag = soup.find('topics')
    topics = []
    for topic in topic_tag.contents:
        topics.append(str(topic.contents[0]))
    return topics


def get_body(soup):
    """
    Gets body of article
    :param soup: article soup
    :return: body text
    """
    body_tag = soup.find('body')
    try:
        return str(body_tag.contents[0])
    except AttributeError:
        return None


def read_article_info(soup):
    """
    Read the information provided about an article
    :param soup: article soup
    :return: article information dictionary
    """
    article_info = {'id': None, 'topics': None, 'body': None}
    article_info['id'] = soup.attrs['newid']
    article_info['topics'] = get_topics(soup)
    article_info['body'] = get_body(soup)
    if article_info['body'] is None:
        return None
    return article_info


def write_article_dict(dict):
    """
    Save article dictionary
    :param dict: article dictionary
    :return:
    """
    file_path = os.path.join(os.path.dirname(__file__), './articles.json')
    if os.path.isfile(file_path):
        os.remove(file_path)
    with open(file_path, 'w') as json_file:
        json.dump(dict, json_file)


def main():
    """
    Main function. performs sgm reading and translating to articles.json
    :return:
    """
    files = find_smg()
    articles = get_all_articles(files)
    article_dict = create_train_test_dict(articles)
    write_article_dict(article_dict)


if __name__ == '__main__':
    main()
