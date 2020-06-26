import parameterization


def _calculate_sqr_distance(a, b):
    """
    Calculate the square distance between two vectors
    :param a: vector a
    :param b: vector b
    :return: square distance
    """
    dst = 0
    for i in range(len(a)):
        dst += (b[i] - a[i]) * (b[i] - a[i])
    return dst


def evaluate(articles, text):
    """
    Evaluate a new text by given train set
    :param articles: train articles
    :param text: text to evaluate
    :return: topic
    """
    smallest_dst = float("inf")
    smallest_topic = None
    for article in articles:
        dst = _calculate_sqr_distance(parameterization.generate_vector_for(text), parameterization.get_vector_for(article))
        if dst < smallest_dst:
            smallest_dst = dst
            smallest_topic = article['topics'][0]
    return smallest_topic
