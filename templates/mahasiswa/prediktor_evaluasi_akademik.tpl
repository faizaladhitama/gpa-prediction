<p id="prediktor-title"> Prediktor Kelulusan Evaluasi Akademik </p>
<div class="container">
		<div class="row prediktor-body">
			<div class="col " id="prediktor-eval-button">
				{% if status == 'lolos' %}
    				<button type="button" class="btn btn-success btn-lg btn3d text-center" data-toggle="modal" data-target="#detailAkademik"><p id="status-prediktor">lolos</p></button>
				{% elif status == 'hati-hati' %}
    				<button type="button" class="btn btn-warning btn-lg btn3d text-center" data-toggle="modal" data-target="#detailAkademik"><p id="status-prediktor">hati-hati</p></button>
				{% else %}
    				<button type="button" class="btn btn-danger btn-lg btn3d  text-center" data-toggle="modal" data-target="#detailAkademik"><p id="status-prediktor">tidak<br> lolos</p></button>
				{% endif %}
			</div>
		</div>

		<div class="row" id="prediktor-message">
			<div class="col text-center">
				{% if status == 'lolos' %}
					<p> Selamat, anda berpeluang <span class ="verdict">{{status}}</span> evaluasi akademik semester {{semester}}!</p>

				{% elif status == 'hati-hati' %}
					<p>Anda harus ber<span class ="verdict">{{status}}</span> untuk  evaluasi akademik <strong>semester {{semester}}</strong>!</p> <p class="prediktor-message">Anda kurang <strong>{{sks_kurang}} SKS </strong> dari <strong>{{sks_seharusnya}} SKS </strong> untuk lolos evaluasi akademik</p>
				{% else %}
					<p>Anda terancam <span class ="verdict">{{status}}</span> evaluasi akademik <strong>semester {{semester}} </strong>!</p>
					<p>Anda kurang <strong>{{sks_kurang}} SKS</strong> dari <strong>{{sks_seharusnya}} SKS</strong> untuk lolos evaluasi akademik</p>
					<p> Harap diskusikan dengan PA anda untuk solusi yang terbaik</p>
				{% endif %}
				<p id="disc">N.b. data yang diolah sampai dengan data pada term 2016/2017-2 </p>

			</div>
		</div>
</div>