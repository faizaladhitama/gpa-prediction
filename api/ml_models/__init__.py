import os.path

import numpy as np
import pandas as pd

from api.ml_models.classifier import Classifier


def get_prediction(nilai):
    nilai = np.asarray(nilai).reshape(1, -1)
    prediksi = Classifier('final')
    prediksi.load_model()
    hasil = prediksi.predict(nilai)
    return hasil


def create_prediction(mata_kuliah, column, fitur):
    model_baru = Classifier(mata_kuliah, column, fitur)
    model_baru.build_model()


def get_prediction_by_matkul(npm, matkul):
    npm = matkul
    matkul = npm


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


def huruf_status_converter(huruf):
    bobot = {
        'A': "lulus",
        'A-': "lulus",
        'B+': "lulus",
        'B': "hati hati",
        'B-': "hati hati",
        'C+': "hati hati",
        'C': "hati hati",
        'C-': "tidak lulus",
        'D': "tidak lulus",
        'E': "tidak lulus",
        'N': "tidak lulus"
    }
    return bobot[huruf]


def load_nilai_df():
    pwd = os.path.dirname(__file__)
    dataframe = pd.read_csv(pwd + '/nilai.csv', delimiter='\t')
    return dataframe


def convert_to_ml_df(dataframe, kd_mk, prasyarats):
    count = 0
    hasil = []
    target_mk = dataframe.loc[dataframe['kd_mk'] == kd_mk]
    if len(target_mk) <= 0:
        return "target not found", False
    for _, row in target_mk.iterrows():
        entry = {}
        no_pras = 1
        for prasyarat in prasyarats:
            flag = dataframe['npm'] == row['npm']
            pras = dataframe.loc[(dataframe['kd_mk'] == prasyarat) & flag]
            if not pras.empty:
                for val in pras['nilai'].values:
                    idx_pras = 'pras' + str(no_pras)
                    entry[idx_pras] = huruf_converter(val)
                    entry['hasil'] = huruf_status_converter(row['nilai'][0])
                    hasil.append(entry)
                    count += 1
            no_pras += 1

    hasil_df = pd.DataFrame(hasil)
    return hasil_df, True


def save_df_csv(dataframe, nama_mk):
    try:
        pwd = os.path.dirname(__file__)
        file_name = pwd + "/data/" + str(nama_mk) + ".csv"
        dataframe.to_csv(file_name, sep=',', index=False)
        return "passed", True
    except FileNotFoundError as exception:
        return exception, False


def create_training_data(kd_mk, nama_mk, prasyarats=None):
    dataframe = load_nilai_df()
    df_hasil = convert_to_ml_df(dataframe, kd_mk, prasyarats)
    if not df_hasil[1]:
        return "Error " + df_hasil[0]
    # df_hasil = df_hasil.dropna() #cleaning na rows
    status = save_df_csv(df_hasil, nama_mk)
    return status


def data_spawner():
    create_training_data("CSC2601105", "MatDas 2", ["UIST601110"])
    create_training_data("CSGE602022", "PPW", ["CSF1600200"])
    create_training_data("CSCM601252", "POK", ["CSC1602500"])
    create_training_data("CSF1600400", "SDA", ["CSF1600200"])
    create_training_data("CSGE603291", "MPPI", ["UIGE600001", "UIGE600002"])
    create_training_data("CSCM602023", "PemLan", ["CSGE601021", "CSGE602022"])
    create_training_data("CSGE602055", "OS", ["CSCM601252"])
    create_training_data("CSCM603154", "JarKom", ["CSGE602055"])
    create_training_data("CSCE604123", "PemFung", ["CSGE602040"])
    create_training_data("CSCM603127", "SysProg", ["CSGE602040", "CSGE602055"])
    create_training_data("CSCE604183", "PBK", ["CSGE602022"])
    create_training_data("CSCM603125", "RPL", ["CSGE601021"])
    create_training_data("CSCM603130", "SC", ["CSGE601010", "CSGE602013", "CSGE602040"])
    create_training_data("CSCM603234", "DSA",
                         ["CSGE602013", "CSGE602070"])
    create_training_data("CSCE604243", "CIS",
                         ["CSCM603154", "CSGE601010", "CSGE601011", "CSGE602013"])
    create_training_data("CSCE604129", "PemPar",
                         ["CSCM602115", "CSGE601021", "CSGE602012", "CSGE602055"])
    create_training_data("CSCM603228", "PPL", ["CSCM603125", "CSGE602070"])
