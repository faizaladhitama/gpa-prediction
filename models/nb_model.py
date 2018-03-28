import pandas as pd
import numpy as np
import pickle
import os.path
from sklearn.preprocessing import Imputer
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

class NbModel:
	def __init__(self, name, columns, num_features):
		self.course_name = str(name)
		self.columns = columns
		self.num_features = num_features
		self.accuracy = 0
		self.clf = GaussianNB()
		self.df = None

	def create_model(self):
		pwd = os.path.dirname(__file__)
		address = pwd+"/data/"+self.course_name+".csv"
		df = pd.read_csv(address, header=None, delimiter=",", engine='python')
		df.columns = self.columns
		df_rev = df

		le = preprocessing.LabelEncoder()
		cat_list = []
		for col in df.columns:
			cat_list.append(le.fit_transform(getattr(df_rev, col)))

		column_cat_value = list(zip(df.columns, cat_list))

		for col in column_cat_value:
			df_rev[col[0]] = col[1]

		self.df = df_rev

		return df_rev

	def train_model(self):
		df = self.df
		scaled_features = {}
		for each in self.num_features:
			mean, std = df[each].mean(), df[each].std()
			scaled_features[each] = [mean, std]
			df.loc[:, each] = (df[each] - mean)/std	

		features = df.values[:,:len(self.num_features)]
		target = df.values[:,len(self.num_features)] #au saya juga bingung , cc Gibran MFW aja
		features_train, features_test, target_train, target_test = train_test_split(features, target, test_size = 0.33, random_state = 10)

		self.clf.fit(features_train, target_train)
		target_pred = self.clf.predict(features_test)
		self.accuracy = accuracy_score(target_test, target_pred, normalize=True)


	def save_model(self):
		pwd = os.path.dirname(__file__)
		file_name = pwd+'/savefile/'+self.course_name+'.sav'
		pickle.dump(self.clf, open(file_name, 'wb'))

	def build_model(self):
		self.create_model()
		self.train_model()
		self.save_model()