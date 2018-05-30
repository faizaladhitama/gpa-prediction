import os.path
import pickle

import pandas as pd
from imblearn.over_sampling import RandomOverSampler, SMOTE
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis, LinearDiscriminantAnalysis
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.linear_model import RidgeClassifierCV
from sklearn.metrics import confusion_matrix, \
    accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.semi_supervised import LabelPropagation, LabelSpreading
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


class Classifier:
    def __init__(self, name, columns=None, num_features=None, md_name="Gaussian"):
        self.model = {
            "Gaussian": GaussianNB(),
            "Bernoulli": BernoulliNB(),
            "Random Forest": RandomForestClassifier(n_estimators=600,
                                                    random_state=10, min_samples_split=3),
            "Extra Tree": ExtraTreesClassifier(n_estimators=600,
                                               random_state=10, min_samples_split=2),
            "Ada Boost": AdaBoostClassifier(n_estimators=600, random_state=10, learning_rate=5),
            "Ada Boost-Decision Tree": AdaBoostClassifier(DecisionTreeClassifier(max_depth=None),
                                                          n_estimators=600,
                                                          learning_rate=2, random_state=10),
            "Gradient Boosting": GradientBoostingClassifier(n_estimators=600,
                                                            learning_rate=0.5, max_depth=None,
                                                            random_state=10),
            "Nearest Neighbor": KNeighborsClassifier(),
            "Linear SVM": SVC(kernel="linear", C=0.025, random_state=10),
            "RBF SVM": SVC(gamma=2, C=1, random_state=10),
            "Gaussian Process": GaussianProcessClassifier(1.0 * RBF(1.0), random_state=10),
            "Decision Tree": DecisionTreeClassifier(max_depth=5, random_state=10),
            "Linear Discriminant": LinearDiscriminantAnalysis(solver="eigen"),
            "Quadratic Discriminant": QuadraticDiscriminantAnalysis(),
            "Nearest Centroid": NearestCentroid(),
            "Ridge": RidgeClassifierCV(),
            "Label Propagation": LabelPropagation(),
            "Label Spreading": LabelSpreading()
        }

        # Classifier berdasarkan nama model
        self.clf = self.model[md_name]
        self.course_name = str(name)
        self.pwd = os.path.dirname(__file__)
        self.file_name = self.pwd + '/savefile/' + self.course_name + '.sav'

        self.build_model()

    def train_model(self):
        data = pd.read_csv(self.pwd + '/final.csv')
        used = data.loc[:, ['mean_pras', 'y']]
        used = used.dropna()
        
        col = 'mean_pras'
        col_zscore = col
        used[col_zscore] = (used[col] -
                            used[col].mean()) / used[col].std(ddof=0)
        target = used['y']
        features = used['mean_pras']
        features_train, _, target_train, _ = \
            train_test_split(features, target, test_size=0.3, random_state=10)

        s_m = SMOTE(random_state=20)
        features_train, target_train = s_m.fit_sample(
            features_train.values.reshape(-1, 1), target_train)

        self.clf.fit(features_train.reshape(-1, 1), target_train)

    def set_model(self, md_name):
        self.clf = self.model[md_name]
        self.build_model()

    def save_model(self):
        pickle.dump(self.clf, open(self.file_name, 'wb'))

    def predict(self, features_test):
        prediction = self.clf.predict(features_test)
        return prediction

    def build_model(self):
        self.train_model()
        self.save_model()
