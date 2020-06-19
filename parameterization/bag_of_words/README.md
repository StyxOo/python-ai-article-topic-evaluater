# Bag of Words

## What is it?
A bag of words represents if a word from a vocabulary appears in a given text. The vocabulary contains all the words we know about.

## How does it work?
First a vocabulary is created from all the articles. It contains all unique words which can be found. This vocuabulary creation is handled by the `vocabulary.py` in the `parameterization` package. Afterwords a vector created for each article. It contains a 0 if a word from the vocabulary is not in the article, and 1 if it is. Let's look at a small example.

> Article 1: This is a small article. It contains many words.  
> Article 2: This article is a bit longer. So it contains more words.

From our two articles, the can create our vocabulary:
> Vocabulary: this, is, a, small, article, it, contains, many, words, bit, longer, so, more

Now we can create our Vectors for each article
> Vector 1: [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0 ]  
> Vector 2: [ 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1 ]

As you can see, we first need to create our vocabulary. this is why we need our articles for training this parameterization. After we have set it up, we can get a vector for any text by using `generate_vetor`. If the new text contains a word which is not listed in the vocabulary, it will be treated as none existent. Because we have no known information about this word, we will not be able to use it for classification anyways. Using our old vocabulary, let's look at an example again:
> Text: This is not an article  
> Vector: [ 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0 ]