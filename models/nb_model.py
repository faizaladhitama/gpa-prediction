from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import Imputer
import numpy as np
import pandas as pdimport picklenm

class Nb_Model:
	def __init__(name, columns, num_features):
		self.course_name = str(name)
		self.columns = columns
		self.num_features = num_features
		self.accuracy = 0
		self.clf = GaussianNB()

	def create_model(self):
		address = "data/"+self.course_name+".csv"
		df = pd.read_csv(address, header=None, delimiter=",", engine='python')
		df.columns = self.columns
		df_rev = df

		le = preprocessing.LabelEncoder()
		cat_list = {}
		for col in df.columns:
			cat_list.append(le.fit_transform(df_rev.col))

		info = list(zip(df.columns, cat_list))

		for col in info(0):
			df_rev[col] = info(1)

		return df_rev

	def train_model(self):
		scaled_features = {}
		for feature in num_features:
			mean, std = df[each].mean(), df[each].std()
			scaled_features[each] = [mean, std]
			df.loc[:, each] = (df[each] - mean)/std	

		feature = df.values[:,:len(self.num_features)]
		target = df.valuse[:,len(self.num_features)] #au saya juga bingung
		features_train, features_test, target_train, target_test = train_test_split(features, target, test_size = 0.33, random_state = 10)

		self.clf.fit(features_train, target_train)
		target_pred = clf.predict(features_test)
		self.accuracy = accuracy_score(target_test, target_pred, normalize=True)


	def saveModel(self):
		file_name = 'savefile/'+self.course_name+'.sav'
		pickle.dump(self.clf, open(file_name, 'wb'))

	def build_model(self):
		self.create_model()
		self.train_model()
		self.saveModel()