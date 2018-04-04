from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

class prediksiEvaluasiAkademik():
	def give_verdict(npm, sks_lulus, sks_diambil, ip):
		status = "Tidak Lolos"
		sks_kemungkinan = sks_lulus + sks_diambil
		if(sks_lulus >= sks_minimal):
			status = "Lolos"
		else if(sks_lulus < sks_minimal and sks_kemungkinan >= sks_minimal):
			status = "Hati Hati"

		return status