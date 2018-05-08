{% extends 'mahasiswa/base-mahasiswa.tpl'%}
{% block contentPage %}
<h3>Total SKS Diperoleh</h3>
<h5>{{all_sks}} SKS</h5>
<div class="col-xs-8">
        <h3> Riwayat SKS</h3>
	    <div class="table-responsive" id="sks-term-table">
			<table class="table table-condensed table-hover table-striped">
				<thead class="table-primary">
					<tr>
						<th>Term</th>
						 <th>Jumlah SKS</th>
					</tr>
				</thead>
				<tbody>
				    {% for key, value in sks_term.items %}
					<tr>
					    <td>{{key}}</td>
					     <td>{{value}}</td>
					</tr>
					{% endfor %}
				</tbody>
		    </table>
		</div>
</div>
 <div class="row ">
	    <div class="col ">
		    <a class="btn btn-link text-center" href="/mahasiswa/">
		        Kembali ke Prediktor
		    </a>
	    </div>
	</div>
{% endblock %}
