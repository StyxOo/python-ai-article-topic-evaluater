# What is this?

This is a small project able to asign topics to a text using AI. It comes with three different parameterization as well as three different classification algorithms. There is a small GUI to make the usage simpler. To run it, simply run `python ui.py` in the main directory.
>You will need python 3 to be able to run the project.

## Why does this exist?
It was created as a semester project for the UIR-E course at the UWB. The assignment can be found in the `seminal_project.pdf`.

## How does it work?
There are three steps involved to make this work.
 - Preprocessing
 - Parameterization
 - Classification  
 
You can learn more about them in the appropriate folders `README.md` files.  
All articles in the `articles_rewritten.json` in the `train` dictionary are used for training. If you want to change which articles are used for training, change it there.

## Requirements
The whole program is written using python 3. Furthermore the [bs4](https://pypi.org/project/beautifulsoup4/) as well as [nltk](https://pypi.org/project/nltk/) packages are required.

## Accuracy
The following table shows the accuracy for each parameterization and classification combination in percent (Determined by evaluating 30 articles from the test set):

 |                    | Bag of Words | Term Frequency | TF-IDF |
 | -----------------: | :----------: | :------------: | :----: |
 | Euclidean Distance | 63           | 63             | 52     |
 | Naive Bayes        | 66           | 66             | 81     |
 | Rocchio            | 55           | 44             | 63     |