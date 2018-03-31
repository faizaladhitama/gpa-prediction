from api.models.nb_model import NbModel

def get_prediction(mata_kuliah, nilai):
	prediksi = NbModel(mata_kuliah,num_features=nilai)
	prediksi.load_model()
	hasil = prediksi.predict(nilai)
	return hasil

def create_prediction(mata_kuliah, column, fitur):
	model_baru = NbModel(mata_kuliah, column, fitur)
	model_baru.build_model()