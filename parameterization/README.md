# Parameterization

## What is it?
It converts a given text into a vector. The resulting vector will be used by the classifier to make predictions about which topic a text belongs to.

## Algorithms
There are three different parameterization algorithms.
 - Bag of Words
 - Term Frequency
 - Term Frequency - Inverted Document Frequency

More information about them can be found in their respective subdirectory.
>It is recommended to read them in order, as they are extending on each other.

## Usage
To make use of one of the parameterizators You can directly hook into it, or make use of the interface in the `__init__.py`. Make sure to first call the `setup_parameterizator` functions to prepare the parameterizer You want to use. For this you will need to provide a name and a set of articles to train on. The namimng is as follows:
 - "bow" for Bag of Words
 - "tf" for Term Frequency
 - "tf_idf" for Term Frequency - Inverted Document Frequency

After a successfull setup, You can create new vector representations for any text using the `get_vector_for` function.  
Most of the parameterizers save their results in json, as it takes quite long to set up all the vectors. It will only create new vectors, if a vector for a given article id does not yet exist, or when you set `force_create` to `True` in the setup step.

> NOTE: If You pull changes from the repository or when changing the parameterization algorithms, make sure to remove their results folders to ensure new vectors are created