import parameterization

from classification import euclidean


def _add_lists(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return c


def _divide_list(a, value):
    for i in range(len(a)):
        a[i] = a[i] / value
    return a


def evaluate(articles, text):
    averages = {}
    for article in articles:
        vector = parameterizer.get_vector_for(article)
        for topic in article['topics']:
            if topic not in averages.keys():
                averages[topic] = []
            averages[topic].append(vector)
    for topic in averages.keys():
        sum = averages[topic][0]
        for i in range(1, len(averages[topic])):
            sum = _add_lists(sum, averages[topic][i])
        avg = _divide_list(sum, len(averages[topic]))
        averages[topic] = avg
    text_vector = parameterizer.get_vector_for(text)
    closest_dst = float("inf")
    closest_topic = None
    for topic in averages.keys():
        dst = euclidean._calculate_sqr_distance(text_vector, averages[topic])
        if dst < closest_dst:
            closest_dst = dst
            closest_topic = topic
    return closest_topic