import requests

API_MAHASISWA = "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/"
API_VERIFY_USER = "https://akun.cs.ui.ac.id/oauth/token/verify/"

def cari_info_program(npm,client_id,access_token):
    print("cari info")
    parameters = {"access_token": access_token, "client_id": client_id}
    response = requests.get(API_MAHASISWA+"cari-info-program/"+npm, params=parameters)
    print ("response => ", response.text)
    print ("response => ", response.json())
    return response.json()

def cari_npm_nama_by_angkatan_prodi(angkatan,prodi,client_id,access_token):
    parameters = {"access_token": access_token, "client_id": client_id}
    response = requests.get(API_MAHASISWA+"cari-npm-nama-by-angkatan-prodi/"+angkatan+"/"+prodi, params=parameters)
    print ("response => ", response.text)
    print ("response => ", response.json())
    return response.json()

def cari_npm_nama_by_kode_kurikulum_kode_mata_kuliah(kd_kurikulum,kd_matkul):
    "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/cari-npm-nama-by-kode-kurikulum-kode-matakuliah/asda/asads/?access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9&client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    pass

def cari_npm_by_nama(query):
    "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/cari-npm-nama/1/?access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9&client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    pass

def count_by_tahun(tahun):
    "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/count-by-tahun/2018/?access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9&client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    pass

def count_lulusan_by_tahun_term(tahun,term):
    "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/count-lulusan-by-tahun-term/2018/1/?access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9&client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    pass

def current_active_period():
    "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/current-active-periode/?access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9&client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    pass

def daftar_lulusan_by_tahun_term(tahun,term):
    "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/daftar-lulusan-by-tahun-term/1/1/?access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9&client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    pass

def summary_repeater_by_matkul_tahun_term(kd_mk,tahun,term):
    #kd_mk,tahun,term
    "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/summary-repeater-by-matkul-tahun-term/1/3/2/?access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9&client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/summary-repeater-by-tahun/2017/?access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9&client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    pass

def jadwal_kelas(npm,tahun,term):
    "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/1506730035/jadwal-kelas/2017/1/?access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9&client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    pass

def presensi(npm,tahun,term):
    "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/1506730035/presensi/2017/1/?access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9&client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    pass

def riwayat(npm,tahun=None,term=None):
    "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/1506730035/riwayat/2017/1/?access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9&client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    pass

def matakuliah_list(kd_kurikulum=None):
    "https://api-dev.cs.ui.ac.id/siakngcs/matakuliah-list/kurikulum/2/?access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9&client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    pass

def matakuliah(id):
    "https://api-dev.cs.ui.ac.id/siakngcs/matakuliah/1/?access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9&client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    pass

def cari_dosen(nama):
    "https://api-dev.cs.ui.ac.id/siakngcs/dosen/nama/Ad/?access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9&client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    pass

def detail_dosen(id):
    "https://api-dev.cs.ui.ac.id/siakngcs/dosen/1/?access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9&client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    pass

def mahasiswa_bimbingan_dosen(id_dosen,tahun=None,term=None):
    "https://api-dev.cs.ui.ac.id/siakngcs/dosen/1/daftar-mahasiswa-bimbingan/2017/1/?access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9&client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    pass

def jadwal_kelas_dosen(id_dosen,tahun,term):
    "https://api-dev.cs.ui.ac.id/siakngcs/dosen/1/jadwal-kelas/2017/1/?access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9&client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    pass