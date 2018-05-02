<h1 class="prediktor-title"> Prediktor Kelulusan Evaluasi Akademik </h1>

<div class="container">
		<div class="row ">
			<div class="col prediktor-body" id="prediktor-eval-button">
				{% if status == 'lolos' %}
    				<a class="btn btn-success btn-lg btn3d prediktor-button" href="/mahasiswa/detail-akademik">lolos</a>
				{% elif status == 'hati-hati' %}
    				<a class="btn btn-warning btn-lg btn3d prediktor-button" href="/mahasiswa/detail-akademik">hati-hati</a>
				{% else %}
    				<a class="btn btn-danger btn-lg btn3d prediktor-red-button" href="/mahasiswa/detail-akademik">tidak<br> lolos</a>
				{% endif %}
			</div>
		</div>

		<div class="row ">
			<div class="col text-center">
				{% if status == 'lolos' %}
					<p class="prediktor-message"> Selamat, anda berpeluang <span class ="verdict">{{status}}</span> evaluasi akademik semester {{semester}}!</p>

				{% elif status == 'hati-hati' %}
					<p class="prediktor-message">Anda harus ber<span class ="verdict">{{status}}</span> untuk  evaluasi akademik semester {{semester}}!</p> <p class="prediktor-message">Anda kurang {{sks_kurang}} dari {{sks_seharusnya}} untuk lolos evaluasi akademik</p>
				{% else %}
					<p class="prediktor-message">Anda terancam <span class ="verdict">{{status}}</span> evaluasi akademik semester {{semester}}!</p>
					<p class="prediktor-message">Anda kurang {{sks_kurang}} dari {{sks_seharusnya}} untuk lolos evaluasi akademik</p>
					<p class="prediktor-message"> Harap diskusikan dengan PA anda untuk solusi yang terbaik</p>
				{% endif %}
			</div>
		</div>

		<div class="row ">
			<div class="col ">
				<a class="btn btn-link text-center" href="/mahasiswa/detail-akademik">
				Lihat Selengkapnya
				</a>
			</div>
		</div>
</div>