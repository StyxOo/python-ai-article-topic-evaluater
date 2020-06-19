# Preprocessing

## What does it do?
It converts the reuters `.sgm` files into a more usable format. The raw files can be found in the `reuters` subfolder. when running it creates two output files. Both of them are in `.json`. They contain a dictionary of all articles marked as `test` and `train`. Articles which were originally marked as `train` but contain no topics, where redirected to the `test` set. If you want to learn more about how the original files are structured, have a look at the `README.txt` inside the `reuters` folder.

## Why do we do this?
to make it easier to work with the files. The original files contain a lot of noise which will not be needed. Furthermore the `.sgm` format is more difficult to work with in Python. It follows a XML like layout which makes quick navigation and debugging more cumbersome. Stemming and lemmatizing allows us to make more accurate predictions, as all words are reduced to their basic main form. 

## What are the results?
The preprocessing will produce two `.json` files. The first one, `articles.json` contains all articles with their `id`, `topics` and `body`. The id reflects the original `NEWID`. The second file is the `articles_rewritten.json`. It is structure in the same way as the first file. The only difference layes in the `body` of the articles. For this second file the `body` has been rewritten. It is no longer the original article, but a list of all the words after lematizing and stemming them, as well as removng all the stopwords.

## How do we get the results?
If you want to run the preprocessing there are two ways to achive this. You can use the GUI and press the button at the very top. If you are planning on making use of the preprocessing without the GUI, you can import the preprocessing package and run `process` from the `__init__.py`. Like this:
```python
import preprocessing

preprocessing.process()
```
If You want more control over what is happening when, You can also run the appropriate steps manually. The script responible for reading the `.sgm` files and creating the `articles.json` is called `sgm_reader.py`. It has a `main` function which goes through all the `.sgm` files in the reuters folder and creates converts them to the `articles.json`. The second step is done by `rewrite.py`. It makes use of the `body_reader.py` for stemming and lemmatizing all the words in an article. 