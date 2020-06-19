_topics = None
_words_per_topic = None


def _get_percent(part, whole):
    return (part / whole) * 100


def _data_total_to_percent(data, total):
    for entry in data:
        data[entry] = _get_percent(data[entry], total)
    return data


def _get_topic_data(articles):
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


def _get_topic_percent_data(articles):
    data, total_topics = _get_topic_data(articles)
    return _data_total_to_percent(data, total_topics)


def _get_topic_word_data(articles):
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


def _get_topic_word_percent_data(articles):
    data = _get_topic_word_data(articles)
    for topic in data:
        total_words = 0
        for word in data[topic]:
            total_words += data[topic][word]
        for word in data[topic]:
            data[topic][word] = _get_percent(data[topic][word], total_words)
    return data


def evaluate(articles, text):
    global _topics, _words_per_topic
    _topics = _get_topic_percent_data(articles)
    _words_per_topic = _get_topic_word_percent_data(articles)

    unique_text = []
    for word in text:
        if word not in unique_text:
            unique_text.append(word)

    highest_probability = 0
    highest_probability_topic = None

    for topic in _topics.keys():
        product = 1
        for word in unique_text:
            if word in _words_per_topic[topic].keys():
                product *= _words_per_topic[topic][word]
            else:
                product *= 1e-15
        product *= _topics[topic]

        if product > highest_probability:
            highest_probability = product
            highest_probability_topic = topic
    return highest_probability_topic