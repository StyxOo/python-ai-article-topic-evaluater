# Term Frequency

## What is it?
the term frequency describes how often a word from a vocabulary appears in a given text.

## How does it work?
It works mostly the same as the bag of words. The main difference is: instead of only keeping track of if a word appears, we keep track of how many times this word appears. Example:
> Vocabulary: this, is, a, small, article, it, contains, many, words, bit, longer, so, more  
> Text: This is a text. This is small. Not many words.  
> Vector: [ 2, 2, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0] 

Just like with the bag of words, we will first have to set up the vocabulary for it to succed.