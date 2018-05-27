<h1 class="prediktor-title-matkul">Prediktor Kelulusan Mata Kuliah</h1>
<h3 class="matkul-to-predict">{{matkul}}</h3>
<div class="container">
<div class="row prediktor-body">
			<div class="col xs-4" id="prediktor-matkul-button">
				{% if status_matkul == 'lulus' %}
    				<button type="button" class="btn btn-success btn-lg btn3d" data-toggle="modal" data-target="#detailAkademik">lolos</button>
				{% elif status_matkul == 'hati-hati' %}
    				<button type="button" class="btn btn-warning btn-lg btn3d " data-toggle="modal" data-target="#detailAkademik">hati-hati</button>
				{% else %}
    				<button type="button" class="btn btn-danger btn-lg btn3d" data-toggle="modal" data-target="#detailAkademik">tidak<br> lolos</button>
				{% endif %}
			</div>
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
					    {% for i in matkul_prasyarat  %}
						<tr>
						    <td>{{i}}</td>
						    <td>{{ value}}</td>
						</tr>
						{% endfor %}
					</tbody>
				</table>
			</div>
		</div>
	</div>

	<div class="row ">
		<div class="col text-center">
					<p> nama prasyarat: {{nama_prasyarat}} </p>

			{% if status_matkul == 'lulus' %}
				<p class="prediktor-message"> Selamat, anda berpeluang <span class ="verdict">{{status_matkul}}</span> <strong>{{matkul}}</strong> !</p>

			{% elif status_matkul == 'hati-hati' %}
				<p class="prediktor-message">Anda harus ber<span class ="verdict">{{status_matkul}}</span> {{matkul}} dalam mengambil mata kuliah <strong> {{matkul}}</strong>!</p> <p class="prediktor-message">Anda harus berusaha keras agar dapat lulus mata kuliah {{matkul}}. Semangat! :)</p>
			{% else %}
				<p class="prediktor-message">Anda terancam <span class ="verdict">{{status_matkul}}</span>  <strong> {{matkul}} </strong>!</p>
				<p class="prediktor-message"> Silakan mengambil mata kuliah yang lain atau diskusikan dengan PA anda untuk solusi yang terbaik</p>
			{% endif %}
		</div>
	</div>
</div>
