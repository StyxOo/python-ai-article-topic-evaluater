from tkinter import *
from ui import widgets

import preprocessing
import parameterization
import classification

"""
this script creates the GUI for the project
"""


def preprocess_callback():
    """
    Starts preprocessing
    :return:
    """
    preprocessing.process()


def set_classifier(name):
    """
    Called when a classifier is selected
    :param name: name of classifier
    :return:
    """
    global classifier, selected_classifier_label
    classifier = name.lower()
    selected_classifier_label.configure(text=name)


def set_parameterizer(name):
    """
    Called when a parameterizer is selected
    :param name: name of parameterizer
    :return:
    """
    global parameterizer
    parameterizer = name.lower()
    selected_parameterizer_label.labelText = name


def select_bayes():
    """
    Select bayes classifier
    :return:
    """
    set_classifier("Bayes")


def select_euclid():
    """
    Select euclid classifier
    :return:
    """
    set_classifier("Euclid")


def select_rocchio():
    """
    Select rocchio classifier
    :return:
    """
    set_classifier("Rocchio")


def select_bow():
    """
    Select bag of words parameterizer
    :return:
    """
    set_parameterizer("BoW")


def select_tf():
    """
    Select term frequency parameterizer
    :return:
    """
    set_parameterizer("TF")


def select_tf_idf():
    """
    Select tf-idf parameterizer
    :return:
    """
    set_parameterizer("TF_IDF")


def evaluate():
    """
    Called when evaluation should be run
    :return:
    """
    if classifier is None:
        print("Make sure to select a classifier")
        return
    if parameterizer is None and classifier != 'bayes':
        print("Make sure to select a parameterizer")
        return

    text = text_input.get("1.0", END)
    if text == "\n":
        print("Make sure you input a text for classification")
        return

    articles = preprocessing.get_train_set()
    if classifier != "bayes":
        parameterization.setup_parameterizator(parameterizer, articles)
    classification.setup_classifier(classifier)
    text = text_input.get("1.0", END)
    topic = classification.evaluate(text, articles)
    topic_label.configure(text=topic)


parameterizer = None
classifier = None


window = Tk()


preprocess_button = Button(text="Preprocess articles", command=preprocess_callback)
preprocess_tooltip = widgets.ToolTip(preprocess_button, "Preprocessing turns the sgm reuter files into usable articles."
                                                        "This only needs to be run the very first time.")
preprocess_button.grid(row=0, column=0, columnspan=4)


classifier_label = Label(text="Classifier:")
classifier_label.grid(row=1, column=0, sticky=W)

selected_classifier_label = Label(text="None")
selected_classifier_label.grid(row=1, column=1, sticky=W)

bayes_select = Button(text="Bayes", command=select_bayes)
bayes_select.grid(row=2, column=0, sticky=W)

euclid_select = Button(text="Euclidean distance", command=select_euclid)
euclid_select.grid(row=3, column=0, sticky=W)

rocchio_select = Button(text="Rocchio", command=select_rocchio)
rocchio_select.grid(row=4, column=0, sticky=W)


parameterizer_label = Label(text="Parameterizer:")
parameterizer_label.grid(row=5, column=0, columnspan=1, sticky=W)

selected_parameterizer_label = Label(text="None")
selected_parameterizer_label.grid(row=5, column=1, sticky=W)

bow_select = Button(text="Bag of Words", command=select_bow)
bow_select.grid(row=6, column=0, sticky=W)

tf_select = Button(text="Term frequency", command=select_tf)
tf_select.grid(row=7, column=0, sticky=W)

tf_idf_select = Button(text="TF - IDF", command=select_tf_idf)
tf_idf_select.grid(row=8, column=0, sticky=W)


evaluate_button = Button(text="Evaluate text", command=evaluate)
evaluate_button.grid(row=9, column=0)


text_label = Label(text="Text:")
text_label.grid(row=1, column=2, columnspan=2, sticky=W)

text_input = Text()
text_input.grid(row=2, column=2, columnspan=2, rowspan=7)


topic_label = Label(text="Topic: ")
topic_label.grid(row=9, column=2, sticky=E)

evaluation_label = Label()
evaluation_label.grid(row=9, column=3, sticky=W)
window.mainloop()
