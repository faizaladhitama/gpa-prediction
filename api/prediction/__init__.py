class Predictor:
	def __init__(self):
		self.path = "../../models/prediction/"

	def set_prediction(self, prediction):
		self.prediction = prediction

	def set_data(self, data):
		self.data = data

	def __check_prediction(self):
		if self.prediction is None:
			raise Exception("Prediction variable is null, please use [set_prediction] to set your prediction")
		elif (self.prediction != "matakuliah") or (self.prediction != "evaluasi"):
			raise Exception("Not valid prediction parameter")
		return True

	def __check_data(self):
		if self.data is None:
			raise Exception("Data variable is null, please use [set_data] to set your data first")
		return True

	def predict(self, matkul):
		self.__check_prediction()
		self.__check_data()

		if self.prediction == "matakuliah":
			return 1

def predict_matkul(matkul, data):
	predictor = Predictor()
	predictor.set_prediction("matakuliah")
	predictor.set_data(data)

	return predict(matkul)
