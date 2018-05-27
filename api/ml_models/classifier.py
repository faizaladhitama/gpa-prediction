import os.path

import pandas as pd
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis, LinearDiscriminantAnalysis
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.metrics import confusion_matrix, \
    accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.linear_model import RidgeClassifierCV
from sklearn.semi_supervised import LabelPropagation, LabelSpreading
from imblearn.over_sampling import RandomOverSampler

class Classifier:
    def __init__(self, name, training_file_name=None, columns=None, num_features=None, md_name="Gaussian"):
        self.model = {
            "Gaussian": GaussianNB(),
            "Bernoulli": BernoulliNB(),
            "Random Forest": RandomForestClassifier(n_estimators=600, random_state=10, min_samples_split=3),
            "Extra Tree": ExtraTreesClassifier(n_estimators=600, random_state=10, min_samples_split=2),
            "Ada Boost": AdaBoostClassifier(n_estimators=600, random_state=10, learning_rate=5),
            "Ada Boost-Decision Tree": AdaBoostClassifier(DecisionTreeClassifier(max_depth=None), n_estimators=600,
                                                          learning_rate=2, random_state=10),
            "Gradient Boosting": GradientBoostingClassifier(n_estimators=600, learning_rate=0.5, max_depth=None,
                                                            random_state=10),
            "Nearest Neighbor": KNeighborsClassifier(),
            "Linear SVM": SVC(kernel="linear", C=0.025, random_state=10),
            "RBF SVM": SVC(gamma=2, C=1, random_state=10),
            "Gaussian Process": GaussianProcessClassifier(1.0 * RBF(1.0), random_state=10),
            "Decision Tree": DecisionTreeClassifier(max_depth=5, random_state=10),
            "Linear Discriminant": LinearDiscriminantAnalysis(solver="eigen"),
            "Quadratic Discriminant": QuadraticDiscriminantAnalysis(),
            "Nearest Centroid":NearestCentroid(),
            "Ridge":RidgeClassifierCV(),
            "Label Propagation":LabelPropagation(),
            "Label Spreading":LabelSpreading()
        }
        print("\nModel :", md_name)
        self.course_name = str(name)
        self.columns = columns
        self.num_features = num_features
        self.clf = self.model[md_name]
        self.pwd = os.path.dirname(__file__)
        if training_file_name is None:
            self.file_name = self.pwd + '/savefile/dt_' + self.course_name + '.sav'
        else:
            self.file_name = self.pwd + '/savefile/' + training_file_name + '.sav'
        self.address = self.pwd + "/data/" + self.course_name + ".csv"
        self.data_frame = pd.read_csv(self.address, header=None, delimiter=",", engine='python')
        self.data_frame.columns = self.columns
        self.data_frame = self.data_frame.iloc[1:, :]

    def normalize_data(self):
        pass

    def train_model_normal_data(self):
        features = self.data_frame.values[:, 1:]
        target = self.data_frame.values[:, 0]
        features_train, features_test, target_train, \
        target_test = train_test_split(features,
                                       target, test_size=0.33, random_state=10)

        self.clf.fit(features_train, target_train)
        target_pred = self.clf.predict(features_test)

        print("\naccuracy without over sampling: {}".format(round(accuracy_score(target_test, target_pred),3)))
        print(confusion_matrix(target_test, target_pred))

    def train_model_with_over_sampling(self):
        ros = RandomOverSampler()
        features = self.data_frame.values[:, 1:]
        target = self.data_frame.values[:, 0]
        x_res, y_res = ros.fit_sample(features, target)
        features_train, features_test, target_train, \
        target_test = train_test_split(x_res,
                                       y_res, test_size=0.33, random_state=10)
        self.clf.fit(features_train, target_train)
        target_pred = self.clf.predict(features_test)

        print("\naccuracy over sampling: {}".format(round(accuracy_score(target_test, target_pred),3)))
        print(confusion_matrix(target_test, target_pred))

    def train_model(self):
        self.train_model_normal_data()
        self.train_model_with_over_sampling()


print("Mata kuliah POK")
c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"])
c.train_model()

c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"], "Bernoulli")
c.train_model()

c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"], "Random Forest")
c.train_model()

c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"], "Extra Tree")
c.train_model()

c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"], "Ada Boost")
c.train_model()

c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"], "Ada Boost-Decision Tree")
c.train_model()

c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"], "Gradient Boosting")
c.train_model()

c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"], "Nearest Neighbor")
c.train_model()

c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"], "Linear SVM")
c.train_model()

c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"], "RBF SVM")
c.train_model()

c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"], "Gaussian Process")
c.train_model()

c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"], "Decision Tree")
c.train_model()

c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"], "Linear Discriminant")
c.train_model()

c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"], "Quadratic Discriminant")
c.train_model()

c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"], "Nearest Centroid")
c.train_model()

c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"], "Ridge")
c.train_model()

c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"], "Label Propagation")
c.train_model()

c = Classifier("POK", "POK", ["hasil", "pras1"], ["pras1"], "Label Spreading")
c.train_model()
