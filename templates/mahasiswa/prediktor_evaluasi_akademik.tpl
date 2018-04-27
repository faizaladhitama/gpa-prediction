<h1 class="prediktor-title"> Prediktor Kelulusan Evaluasi Akademik </h1>

<div class="container">
		<div class="row ">
			<div class="col prediktor-body" id="prediktor-eval-button">
				{% if status == 'lolos' %}
    				<button type="button" class="btn btn-success btn-lg btn3d" data-toggle="modal" data-target="#detailAkademik">lolos</button>
				{% elif status == 'hati-hati' %}
    				<button type="button" class="btn btn-warning btn-lg btn3d" data-toggle="modal" data-target="#detailAkademik">hati-hati</button>
				{% else %}
    				<button type="button" class="btn btn-danger btn-lg btn3d" data-toggle="modal" data-target="#detailAkademik">tidak <br>lolos</button>
				{% endif %}
			</div>
		</div>

		<div class="row ">
			<div class="col">
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
			<div class="col">
				<button type="button" class="btn btn-link" data-toggle="modal" data-target="#detailAkademik">
				Lihat Selengkapnya
				</button>
			</div>
		</div>
</div>