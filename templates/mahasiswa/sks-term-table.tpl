{% extends 'mahasiswa/base-mahasiswa.tpl'%}
{% block contentPage %}
<h3 class="text-center mt-5"> Riwayat SKS</h3>
<div class="container mx-auto my-3" id="myTabContent2">
	<h4 class="font-weight-bold">Total SKS Diperoleh</h4>
	<h5>{{all_sks}} SKS</h5>
	<div class="col-xs-8 mt-5">
	        <h4 class="font-weight-bold"> Riwayat SKS</h4>
		    <div class="table-responsive" id="sks-term-table">
				<table class="table table-condensed table-hover table-striped">
					<thead class="table-primary">
						<tr>
							<th>Term</th>
							 <th>Jumlah SKS</th>
						</tr>
					</thead>
					<tbody>
					    {% for i in sks_term %}
						<tr>
						    <td>{{i.0}}</td>
						     <td>{{i.1}}</td>
						</tr>
						{% endfor %}
					</tbody>
			    </table>
			</div>
	</div>
	<div class="row ">
	    <div class="col ">
		      <a href="/mahasiswa" role="button" class="btn btn-info btn-arrow-left my-3">Kembali ke Prediktor</a>
		      <a href="/mahasiswa/peraturan-akademik" role="button" class="btn btn-danger btn-arrow-left my-3">
		      Peraturan Akademik</a>
		      <a href="/mahasiswa/riwayat-ip" role="button" class="btn btn-success btn-arrow-left my-3">Riwayat IP</a>
	    </div>
	</div>
</div>
{% endblock %}
