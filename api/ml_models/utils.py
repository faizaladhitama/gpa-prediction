import api.ml_models.nb_model

def search_matkul(request, nama_mk):
	npm = request.session['kode_identitas']
	kd_mk = convert_nama_to_kode(nama_mk)
	list_matkul = {
		"CSF1600200": None,
		"UIST601111": None,
		"UIST601110": None,
		"CSF1600100": None,
		"UIGE600002": None,
		"CSF1600103": None,
		"CSC1602106": None,
		"UIGE600001": None,
		"CSC1602500": None,
		"CSF1600400": ["CSF1600200"],
		"CSC2601105": ["UIST601110"],
		"CSGE601011": None,
		"UIGE600010": None,
		"UIGE600003": None,
		"UIGE600020": None,
		"CSCM601252": ["CSCM601150"],
		"CSGE602022": ["CSGE601020"],
		"CSF2600102": None,
		"CSCM603217": ["CSCM602115", "CSGE602012"],
		"CSGE602070": ["CSGE601021"],
		"CSGE603291": ["UIGE600001", "UIGE600002"],
		"CSCM602023": ["CSGE601021", "CSGE602022"],
		"CSGE602055": ["CSCM601252"],
		"CSCM602241": ["CSGE601010", "CSGE601011"],
		"CSCM603154": ["CSGE602055"],
		"CSCE604123": ["CSGE602040"],
		"CSCM603127": ["CSGE602040", "CSGE602055"],
		"CSCE604183": ["CSGE602022"],
		"CSCM603125": ["CSGE601021"],
		"CSCM603130": ["CSGE601010", "CSGE602013", "CSGE602040"],
		"CSCM603234": ["CSGE602013", "CSGE602070"],
		"CSCE604243": ["CSCM603154", "CSGE601010", "CSGE601011", "CSGE602013"],
		"CSCM603228": ["CSCM603125", "CSGE602070"],
		"CSCE604129": ["CSCM602115", "CSGE601021", "CSGE602012", "CSGE602055"]
	}

	pras = list_matkul[kd_mk]
	arr_col = ["hasil"]
	pras_col = []

	# dapetin kolom
	for i in range(len(pras)):
		arr_col.append("pras"+(i+1))
		pras_col.append("pras"+(i+1))
	model = nb_model.NbModel(nama_mk,arr_col,pras_col)
	model.build_model()

	test = []
	# dapetin nilai prasyarat
	for i in range(len(pras)):
		test.append(db.access(npm,pras[i]))
	return model.predict(test)