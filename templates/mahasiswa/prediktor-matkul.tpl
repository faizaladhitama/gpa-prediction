{% extends 'mahasiswa/base-mahasiswa.tpl'%}
{% block contentPage %}
<div class="container mt-5">
    <div class="row">
        <div class="col">
            <div class="col-12 mt-5">
                <h1 class="text-center search-bar">Cari Mata Kuliah</h1>
            </div>
            <form class="form-inline row" action="{% url 'mahasiswa:query-checker' %}" method="POST">
                {% csrf_token %}
                <div class="container-fluid">
                    <div class="row mt-3">
                        <input class="form-control col-4 my-2 my-sm-0 mx-auto" type="search" name="matkul" id="matkul" placeholder="Tuliskan nama mata kuliah yang akan diprediksi" aria-label="Search">
                    </div>
                <div class="row mt-3">
                    <button class="btn btn-info my-2 my-sm-0 mx-auto" type="submit">Cari <i class="fa fa-search"></i></button>
                </div>
                </div>
            </form>
        </div>
    </div>
</div>
<div class="container">
{% if matkul_prasyarat == 'Mata Kuliah atau Prasyarat Tidak Ditemukan' %}
    <div class="alert alert-danger text-center">
    <strong>Mohon maaf, </strong> Mata Kuliah <strong>{{matkul}}</strong>
    atau Prasyarat dari <strong>{{matkul}}</strong> Tidak Ditemukan.
</div>
<div class="container mt-5">
{% else %}
<h1 class="prediktor-title-matkul">Prediktor Kelulusan Mata Kuliah</h1>
<h3 class="matkul-to-predict">{{matkul}}</h3>
<div class="container">
<div class="row prediktor-body">
			<div class="col xs-4" id="prediktor-matkul-button">
				{% if status_matkul == 'lulus' %}
    				<button type="button" class="btn btn-success btn-lg btn3d" data-toggle="modal" data-target="#detailAkademik">lulus</button>
				{% elif status_matkul == 'hati hati' %}
    				<button type="button" class="btn btn-warning btn-lg btn3d " data-toggle="modal" data-target="#detailAkademik">hati-hati</button>
    				}
				{% else %}
    				<button type="button" class="btn btn-danger btn-lg btn3d" data-toggle="modal" data-target="#detailAkademik">tidak<br> lulus</button>
					}
				{% endif %}
			</div>
	</div>

	<div class="row ">
		<div class="col text-center">
			{% if status_matkul == 'lulus' %}
				<p class="prediktor-message"> Selamat, anda berpeluang <span class ="verdict">{{status_matkul}}</span> <strong>{{matkul}}</strong> !</p>

			{% elif status_matkul == 'hati hati' %}
				<p class="prediktor-message">Anda harus ber<span class ="verdict">{{status_matkul}}</span> {{matkul}} dalam mengambil mata kuliah <strong> {{matkul}}</strong>!</p> <p class="prediktor-message">Anda harus berusaha keras agar dapat lulus mata kuliah {{matkul}}. Semangat! :)</p>
			{% else %}
				<p class="prediktor-message">Anda terancam <span class ="verdict">{{status_matkul}}</span>  <strong> {{matkul}} </strong>!</p>
				<p class="prediktor-message"> Silakan mengambil mata kuliah yang lain atau diskusikan dengan PA anda untuk solusi yang terbaik</p>
			{% endif %}
		</div>
	</div>
</div>
{% endif %}
{% endblock %}
{% block modal%}
{% include 'mahasiswa/prasyarat-modal.tpl' %}
{% endblock%}