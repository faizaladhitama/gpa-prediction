<h1 class="prediktor-title"> Prediktor Kelulusan Evaluasi Akademik </h1>

<div class="container">
		<div class="row ">
			<div class="col prediktor-body" id="prediktor-eval-button">
				{% if status == 'lolos' %}
    				<button type="button" class="btn btn-success btn-lg btn3d">lolos</button>
				{% elif status == 'hati-hati' %}
    				<button type="button" class="btn btn-warning btn-lg btn3d">hati-hati</button>
				{% else %}
    				<button type="button" class="btn btn-success btn-lg btn3d">tidak <br>lolos</button>
				{% endif %}
			</div>
		</div>

		<div class="row ">
			<div class="col">
				<p class="prediktor-message"> Selamat, anda berpeluang <span class ="verdict">lolos</span> evaluasi akademik semester 2!<p>
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