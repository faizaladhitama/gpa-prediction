import os.path
import pickle
import pandas as pd
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from imblearn.over_sampling import RandomOverSampler

class NbModel:
    def __init__(self, name, columns=None, num_features=None):
        self.course_name = str(name)
        self.columns = columns
        self.num_features = num_features
        self.accuracy = -1
        self.clf = GaussianNB()
        self.data_frame = None

    def create_model(self):
        pwd = os.path.dirname(__file__)
        address = pwd + "/data/" + self.course_name + ".csv"
        data_frame = pd.read_csv(address, header=None, delimiter=",", engine='python')
        data_frame.columns = self.columns
        df_rev = data_frame

        label_encode = preprocessing.LabelEncoder()
        cat_list = []
        for col in data_frame.columns:
            cat_list.append(label_encode.fit_transform(getattr(df_rev, col)))

        column_cat_value = list(zip(data_frame.columns, cat_list))

        for col in column_cat_value:
            df_rev[col[0]] = col[1]

        self.data_frame = df_rev

        return df_rev

    def train_model(self):

        data_frame = self.data_frame
        scaled_features = {}
        try:
            for each in self.num_features:
                mean, std = data_frame[each].mean(), data_frame[each].std()
                scaled_features[each] = [mean, std]
                data_frame.loc[:, each] = (data_frame[each] - mean) / std
            features = data_frame.values[:, 1:]
            target = data_frame.values[:, 0]
        except TypeError:
            return "TypeError has Occured , try run obj.create_model"

        features_train, features_test, target_train, \
        target_test = train_test_split(features,
                                       target, test_size=0.3, random_state=10)

        self.clf.fit(features_train, target_train)
        target_pred = self.clf.predict(features_test)
        self.accuracy = accuracy_score(target_test, target_pred, normalize=True)
        print("Non over sampling acc :", self.accuracy)

        ros = RandomOverSampler()
        x_res, y_res = ros.fit_sample(features_train, target_train)
        features_train, features_test, target_train, \
        target_test = train_test_split(x_res,
                                       y_res, test_size=0.3, random_state=10)
        self.clf.fit(features_train, target_train)
        target_pred = self.clf.predict(features_test)
        self.accuracy = accuracy_score(target_test, target_pred, normalize=True)
        print("Over sampling acc :", self.accuracy)
        return None

    def save_model(self):
        pwd = os.path.dirname(__file__)
        file_name = pwd + '/savefile/' + self.course_name + '.sav'
        pickle.dump(self.clf, open(file_name, 'wb'))

    def load_model(self):
        pwd = os.path.dirname(__file__)
        file_name = pwd+'/savefile/'+self.course_name+'.sav'
        self.clf = pickle.load(open(file_name, 'rb'))

    def predict(self, features_test):
        prediction = self.clf.predict(features_test)
        return prediction

    def build_model(self):
        self.create_model()
        self.train_model()
        self.save_model()

# from api.models.nb_model import *
# model = NbModel("POK", ["hasil", "pras1"], ["pras1"])
# model.build_model()
