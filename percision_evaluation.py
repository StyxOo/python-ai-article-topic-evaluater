import preprocessing
import parameterization
import classification

"""
This script evaluates the accuracy of all parameterization and classification combinations
"""
if __name__ == '__main__':
    parameterizers = ["bow", "tf", "tf_idf"]
    classifiers = ["euclid", "bayes", "rocchio"]

    train_articles = preprocessing.get_train_set()
    test_articles = preprocessing.get_test_set()

    for p in parameterizers:
        parameterization.setup_parameterizator(p, train_articles)
        for c in classifiers:
            classification.setup_classifier(c)

            total = 0
            correct = 0
            cap = 2
            for i in range(len(test_articles)):
                if i > cap:
                    break
                print("Evaluate article {0}".format(i))
                a = test_articles[i]
                topic = classification.evaluate(a['body'], train_articles, True)
                if topic in a['topics']:
                    correct += 1
                total += 1
            print("Combination of '{0}' and '{1}' results in {2} correct of {3}.".format(p, c, correct, total))
