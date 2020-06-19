import parameterization


def _calculate_sqr_distance(a, b):
    dst = 0
    for i in range(len(a)):
        dst += (b[i] - a[i]) * (b[i] - a[i])
    return dst


def evaluate(articles, text):
    smallest_dst = float("inf")
    smallest_topic = None
    for article in articles:
        dst = _calculate_sqr_distance(parameterizer.get_vector_for(text), parameterizer.get_vector_for(article))
        if dst < smallest_dst:
            smallest_dst = dst
            smallest_topic = article['topics'][0]
    return smallest_topic
