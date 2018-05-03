import numpy as np
from api.models.nb_model import NbModel


def get_prediction(mata_kuliah, nilai):
    nilai = np.asarray(nilai).reshape(1, -1)
    prediksi = NbModel(mata_kuliah, num_features=nilai)
    prediksi.load_model()
    hasil = prediksi.predict(nilai)
    return hasil

def create_prediction(mata_kuliah, column, fitur):
    model_baru = NbModel(mata_kuliah, column, fitur)
    model_baru.build_model()

def get_prediction_by_matkul(npm, matkul):
    pass

def huruf_converter(huruf):
    bobot = {
        'A': 4.00,
        'A-': 3.70,
        'B+': 3.30,
        'B': 3.00,
        'B-': 2.70,
        'C+': 2.30,
        'C': 2.00,
        'C-': 1.70,
        'D': 1.00,
        'E': 0.00,
        'N': 0.00
    }
    return bobot[huruf]

def convert_to_ml_df(kd_mk, prasyarats):
    count = 0
    hasil = []
    target_mk = df.loc[df['kd_mk'] == kd_trgt]
    if(len(target_mk) > 0):
    	return "target not found", False
    for index, row in target_mk.iterrows():
        entry={}
        no_pras = 1
        for prasyarat in prasyarats:
            pras = df.loc[(df['kd_mk'] == prasyarat) & (df['npm'] == row['npm'])]
            if(len(pras) > 0):
                for val in pras['nilai'].values:
                    idx_pras = 'pras'+str(no_pras)
                    entry[idx_pras] = huruf_converter(val)
                    entry['nilai'] = huruf_converter(row['nilai'][0])
                    hasil.append(entry)
                    count += 1
            no_pras += 1

    hasil_df = pd.DataFrame(hasil)
    return hasil_df, True
