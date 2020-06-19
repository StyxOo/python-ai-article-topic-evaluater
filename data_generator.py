def get_percent(part, whole):
    return (part / whole) * 100


def data_total_to_percent(data, total):
    for entry in data:
        data[entry] = get_percent(data[entry], total)
    return data


def get_topic_data(articles):
    data = {}
    total_topics = 0
    for article in articles:
        for topic in article['topics']:
            total_topics += 1
            if topic in data:
                data[topic] += 1
            else:
                data[topic] = 1
    return data, total_topics


def get_topic_percent_data(articles):
    data, total_topics = get_topic_data(articles)
    return data_total_to_percent(data, total_topics)


def get_word_data(articles):
    data = {}
    total_words = 0
    for article in articles:
        words = article['body']
        for word in words:
            total_words += 1
            if word in data:
                data[word] += 1
            else:
                data[word] = 1
    return data, total_words


def get_word_percent_data(articles):
    data, total_words = get_word_data(articles)
    return data_total_to_percent(data, total_words)


def get_topic_word_data(articles):
    data = {}
    for article in articles:
        for topic in article['topics']:
            if topic not in data:
                data[topic] = {}
            for word in article['body']:
                if word in data[topic]:
                    data[topic][word] += 1
                else:
                    data[topic][word] = 1
    return data


def get_topic_word_percent_data(articles):
    data = get_topic_word_data(articles)
    for topic in data:
        total_words = 0
        for word in data[topic]:
            total_words += data[topic][word]
        for word in data[topic]:
            data[topic][word] = get_percent(data[topic][word], total_words)
    return data
