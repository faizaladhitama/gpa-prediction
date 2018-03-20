import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import Imputer
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

pok_df = pd.read_csv("data/pok.csv", header=None, delimiter=",", engine='python')
pok_df.columns = ['nilaiDDP', 'nilaiPSD', 'absensiDDP', 'absensiPSD', 'IP', 'status']

pok_df_rev = pok_df

le = preprocessing.LabelEncoder()
nilaiDDP_cat = le.fit_transform(pok_df.nilaiDDP)
nilaiPSD_cat = le.fit_transform(pok_df.nilaiPSD)
absensiDDP_cat = le.fit_transform(pok_df.absensiDDP)
absensiPSD_cat = le.fit_transform(pok_df.absensiPSD)
ip_cat = le.fit_transform(pok_df.IP)
status_cat = le.fit_transform(pok_df.status)

pok_df_rev['nilaiDDP'] = nilaiDDP_cat
pok_df_rev['nilaiPSD'] = nilaiPSD_cat
pok_df_rev['absensiDDP'] = absensiDDP_cat
pok_df_rev['absensiPSD'] = absensiPSD_cat
pok_df_rev['IP'] = ip_cat
pok_df_rev['status'] = status_cat


num_feature = ['nilaiDDP', 'nilaiPSD', 'absensiDDP', 'absensiPSD', 'IP']
scaled_features = {}
for each in num_feature:
	mean, std = pok_df_rev[each].mean(), pok_df_rev[each].std()
	scaled_features[each] = [mean, std]
	pok_df_rev.loc[:, each] = (pok_df_rev[each] - mean)/std

features = pok_df_rev.values[:,:5]
target = pok_df_rev.values[:,5]
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size = 0.33, random_state = 10)

clf = GaussianNB()
clf.fit(features_train, target_train)
target_pred = clf.predict(features_test)
print(accuracy_score(target_test, target_pred, normalize=True))

filename = 'savefile/pok_model.sav'
pickle.dump(clf, open(filename, 'wb'))

