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
