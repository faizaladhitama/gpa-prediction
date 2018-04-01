<h1 class="prediktor-title">Prediktor Kelulusan Mata Kuliah</h1>
<h3 class="matkul-to-predict">Proyek Perangkat Lunak</h3>
<div class="container">
		<div class="row prediktor-body">
			<div class="col-xs-4" id="result-button">
				{% load static %} 
				<img src= "{% static "assets/yellowButton.png" %}">
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
			<div class="col">
				<p class="prediktor-message"> Hati-hati! Anda memiliki kemungkinan  <span class ="verdict">tidak lulus</span> Proyek Perangkat Lunak <p>
			</div>
		</div>
</div>
