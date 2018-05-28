import os.path

import numpy as np
import pandas as pd

from api.ml_models.classifier import Classifier

def matkul_converter(matkul):
    convert_map = {
        'Administrasi Sistem': 4,
        'Analisis Numerik': 5,
        'Aproksimasi & Sistem Nonlinier': 6,
        'Basis Data': 7,
        'Basis Data Lanjut': 8,
        'Bioinformatika': 9,
        'Customer Relationship Management': 10,
        'Dasar-Dasar Arsitektur Komputer': 11,
        'Dasar-Dasar Audit SI': 12,
        'Desain & Analisis Algoritma': 13,
        'E-Commerce': 14,
        'Enterprise Resource Planning': 15,
        'Game Development': 16,
        'Geometri Komputasional': 17,
        'Grafika Komputer': 18,
        'Infrastruktur TI Modern': 19,
        'Jaringan Komputer': 20,
        'Jaringan Komunikasi Data': 21,
        'Jejaring Semantik': 22,
        'Kecerdasan Bisnis': 23,
        'Komputasi Lunak': 24,
        'Komputasi Ubiquitous & Net-Sentris': 25,
        'Konfigurasi ERP': 26,
        'Kriptografi & Keamanan Informasi': 27,
        'Layanan & Aplikasi Web': 28,
        'Logika Komputasional': 29,
        'Manajemen Hubungan Pelanggan': 30,
        'Manajemen Keamanan Informasi': 31,
        'Manajemen Layanan TI': 32,
        'Manajemen Proyek TI': 33,
        'Manajemen Rantai Suplai': 34,
        'Manajemen Sistem Informasi': 35,
        'Manajemen Sumber Daya Manusia': 36,
        'Metode Formal': 37,
        'Organisasi Sistem Komputer': 38,
        'Pemelajaran Mesin': 39,
        'Pemrograman Deklaratif': 40,
        'Pemrograman Konkuren & Paralel': 41,
        'Pemrograman Logika': 42,
        'Pemrograman Sistem': 43,
        'Penambangan Data': 44,
        'Pengajaran Berbantuan Komputer': 45,
        'Pengantar Organisasi Komputer': 46,
        'Pengembangan dan Pemasaran Produk': 47,
        'Pengolahan Bahasa Manusia': 48,
        'Pengolahan Citra': 49,
        'Pengolahan Multimedia': 50,
        'Pengolahan Sinyal Dijital': 51,
        'Penjaminan Mutu Perangkat Lunak': 52,
        'Perancangan & Pemrograman Web': 53,
        'Perdagangan Elektronis': 54,
        'Perolehan Informasi': 55,
        'Persamaan Diferensial': 56,
        'Proyek Pengembangan Sistem Informasi': 57,
        'Proyek Perangkat Lunak': 58,
        'Rancangan Sistem Dijital': 59,
        'Rekayasa Perangkat Lunak': 60,
        'Riset Operasi': 61,
        'Robotika': 62,
        'Simulasi & Pemodelan': 63,
        'Sistem Cerdas': 64,
        'Sistem Informasi Akuntansi dan Keuangan': 65,
        'Sistem Informasi Geografis': 66,
        'Sistem Interaksi': 67,
        'Sistem Operasi': 68,
        'Sistem Terdistribusi': 69,
        'Sistem Tertanam': 70,
        'Struktur Data & Algoritma': 71,
        'Teknik Kompilator': 72,
        'Teknologi Mobile': 73,
        'Teori Bahasa & Automata': 74,
        'Teori Informasi': 75
    }
    return convert_map[matkul]

def get_prediction(pras1, pras2, pras3, pras4, nama_matkul):
    pras_mean = np.mean([pras1, pras2, pras3, pras4])
    pras_median = np.median([pras1, pras2, pras3, pras4])
    pras_std = np.std([pras1, pras2, pras3, pras4])
    pras_num = np.count_nonzero([pras1, pras2, pras3, pras4])
    input_model = np.zeros(76)
    
    input_model[0] = pras_mean
    input_model[1] = pras_median
    input_model[2] = pras_std
    input_model[3] = pras_num
    input_model[matkul_converter(nama_matkul)] = 1
    
    prediksi = Classifier('final')
    prediksi.load_model()
    hasil = prediksi.predict(input_model.reshape(1, -1))
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
