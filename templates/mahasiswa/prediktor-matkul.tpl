<h1 class="prediktor-title-matkul">Prediktor Kelulusan Mata Kuliah</h1>
<h3 class="matkul-to-predict">{{matkul}}</h3>
<div class="container">
<div class="row ">
			<div class="col prediktor-body" id="prediktor-eval-button">
				{% if status_matkul == 'lulus' %}
    				<button type="button" class="btn btn-success btn-lg btn3d prediktor-button" data-toggle="modal" data-target="#detailAkademik">lolos</button>
				{% elif status_matkul == 'hati-hati' %}
    				<button type="button" class="btn btn-warning btn-lg btn3d prediktor-button" data-toggle="modal" data-target="#detailAkademik">hati-hati</button>
				{% else %}
    				<button type="button" class="btn btn-danger btn-lg btn3d prediktor-red-button" data-toggle="modal" data-target="#detailAkademik">tidak<br> lolos</button>
				{% endif %}
			</div>
		</div>
		<p>ini status loh {{status_matkul}}</p>
		<div class="row ">
			<div class="col text-center">
				{% if status_matkul == 'lolos' %}
					<p class="prediktor-message"> Selamat, anda berpeluang <span class ="verdict">{{status_matkul}}</span> {{matkul}} !</p>

				{% elif status_matkul == 'hati-hati' %}
					<p class="prediktor-message">Anda harus ber<span class ="verdict">{{status_matkul}}</span> {{matkul}} <strong> {{semester}}</strong>!</p> <p class="prediktor-message">Anda kurang <strong>{{sks_kurang}} SKS </strong> dari <strong>{{sks_seharusnya}} SKS </strong> untuk lolos evaluasi akademik</p>
				{% else %}
					<p class="prediktor-message">Anda terancam <span class ="verdict">{{status_matkul}}</span>  <strong> {{matkul}} </strong>!</p>
					<p class="prediktor-message"> Harap diskusikan dengan PA anda untuk solusi yang terbaik</p>
				{% endif %}
			</div>
		</div>
		<div class="row prediktor-body">
			<div class="col-xs-8"> 
				<div class="table-responsive" id="table-matkul-prasyarat">
					<table class="table table-condensed table-hover table-striped">
						<thead class="table-primary">
						<tr>
						  <th>Mata Kuliah Prasyarat</th>
						  <th>Nilai</th>
						</tr>
						</thead>
						<tbody>
							<tr>
							  <td>DDP</td>
							  <td>C</td>
							</tr>
							<tr>
							  <td>RPL</td>
							  <td>B-</td>
							</tr>
							<tr>
							  <td>Basis Data</td>
							  <td>C</td>
							</tr>
							<tr>
							  <td>Jaringan Komputer</td>
							  <td>C</td>
							</tr>
							<tr>
							  <td>PPW</td>
							  <td>B-</td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>
		</div>

		<div class="row">
			<div class="col text-center">
				<p class="prediktor-message"> Hati-hati! Anda memiliki kemungkinan  <span class ="verdict">tidak lulus</span> Proyek Perangkat Lunak <p>
			</div>
		</div>
</div>
