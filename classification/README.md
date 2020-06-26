# Classification

## What does it do?
A classifier will determine the topic a text belongs to. It uses three different methods to do so.
 - Naive Bayes
 - Euclidean Distance
 - Rocchio

The Euclidean Distance as well as Rocchio make use of the parameterizers. Naive Bayes does its own thing. To read more about them, check the appropriate subdirectories

## Usage
To make use of one of the classifiers You can directly hook into it, or make use of the interface in the `__init__.py`. Make sure to first call the `setup_classifer` functions to prepare the classifier You want to use. For this you will need to provide a name. The naming is as follows:
 - "bayes" for Naive Bayes
 - "euclid" for euclidean Distance
 - "rocchio" for Rocchio

After a successfull setup, You can evaluate any given text using the `evaluate` function. This function also makes use of the `body_reader.py`, which can be found in the preprocessing package, for stemming lemmatizing the words.
> NOTE: If you want to use Euclidean Distance or Rocchio for classification, make sure to set up a parameterizator first.