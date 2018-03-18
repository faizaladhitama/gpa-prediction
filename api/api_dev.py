import requests

API_BASE = "https://api-dev.cs.ui.ac.id/siakngcs/"
API_MAHASISWA = "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/"
API_VERIFY_USER = "https://akun.cs.ui.ac.id/oauth/token/verify/"

def cari_info_program(npm, client_id, access_token):
    print("cari info")
    parameters = {"access_token": access_token, "client_id": client_id}
    response = requests.get(API_MAHASISWA+"cari-info-program/"+npm, params=parameters)
    print("response => ", response.text)
    print("response => ", response.json())
    return response.json()

def cari_npm_nama_by_angkatan_prodi(angkatan, prodi, client_id, access_token):
    parameters = {"access_token": access_token, "client_id": client_id}
    response = requests.get(API_MAHASISWA+"cari-npm-nama-by-angkatan-prodi/"+angkatan+"/"+prodi,
                            params=parameters)
    print("response => ", response.text)
    print("response => ", response.json())
    return response.json()

def acs_cred():
    client_id = "client_id=X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG"
    access_token = "access_token=DoGHePHO0Nug23EHpks9Lr56u3EZc9"
    return access_token+"&"+client_id

def cari_npm_nama_by_kode_kurikulum_kode_mata_kuliah(kd_kurikulum, kd_matkul):
    API_BASE + "mahasiswa/cari-npm-nama-by-kode-kurikulum-kode-matakuliah/asda/asads/?"+acs_cred()

def cari_npm_by_nama(query):
    link = API_BASE + "mahasiswa/cari-npm-nama/1/?"+acs_cred()

def count_by_tahun(tahun):
    API_BASE + "mahasiswa/count-by-tahun/2018/?"+acs_cred()

def count_lulusan_by_tahun_term(tahun, term):
    link = API_BASE + "mahasiswa/count-lulusan-by-tahun-term/2018/1/?"+acs_cred()

def current_active_period():
    link = API_BASE + "mahasiswa/current-active-periode/?"+acs_cred()

def daftar_lulusan_by_tahun_term(tahun, term):
    link = API_BASE + "mahasiswa/daftar-lulusan-by-tahun-term/1/1/?"+acs_cred()

def summary_repeater_by_matkul_tahun_term(kd_mk, tahun, term):
    #kd_mk,tahlink = un,term
    link_matkul = API_BASE + "mahasiswa/summary-repeater-by-matkul-tahun-term/1/3/2/?"+acs_cred()
    link_term = API_BASE + "mahasiswa/summary-repeater-by-tahun/2017/?"+acs_cred()

def jadwal_kelas(npm, tahun, term):
    link = API_BASE + "mahasiswa/1506730035/jadwal-kelas/2017/1/?"+acs_cred()

def presensi(npm, tahun, term):
    link = API_BASE + "mahasiswa/1506730035/presensi/2017/1/?"+acs_cred()

def riwayat(npm, tahun=None, term=None):
    link = API_BASE + "mahasiswa/1506730035/riwayat/2017/1/?"+acs_cred()

def matakuliah_list(kd_kurikulum=None):
    link = API_BASE + "matakuliah-list/kurikulum/2/?"+acs_cred()

def matakuliah(id):
    link = API_BASE + "matakuliah/1/?"+acs_cred()
    
def cari_dosen(nama):
    link = API_BASE + "dosen/nama/Ad/?"+acs_cred()
    
def detail_dosen(id):
    link = API_BASE + "dosen/1/?"+acs_cred()

def mahasiswa_bimbingan_dosen(id_dosen, tahun=None, term=None):
    link = API_BASE + "dosen/1/daftar-mahasiswa-bimbingan/2017/1/?"+acs_cred()

def jadwal_kelas_dosen(id_dosen, tahun, term):
    link = API_BASE + "dosen/1/jadwal-kelas/2017/1/?"+acs_cred()
