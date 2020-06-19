# Naive Bayes

## Who does it work?
Naive Bayers works by using probabilities. In our case two probabilities are calculated. The probability for a topic as well as the probabilty for a word to be in a specific topic. To calculate the probabilty of a topic, the total number of topics, as well as how often each topic occurs are gathered. Then we can divide the number of how often a topic occurs by the total number of topics to get a percentage of how likely a topic is. To determine the probability of a word to be in a topic, we count the occurences of each word in each topic and divide it by our tota number of words in the topic. To classify a new text, we go through all the topics and multiply the applicable words probabilities with each other, for each word in the new text. This product is multiplied with the probability for the topic. Whichever topic produces the highest probability, is the topic of our text.

## How do we use it?
To use Naive Bayes we can simply call the `evaluate` function and pass the training articles as well as the new text. As it does not rely on any of our parameterization algorithms, no setup for them is required.