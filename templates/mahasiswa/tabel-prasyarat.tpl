  <div class="modal fade" id="tabelPrasyarat">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
            <h4 class="modal-title">Tabel Nilai Mata Kuliah Prasyarat</h4>
            <button type="button" class="close" data-dismiss="modal">&times;</button>
        </div>
      <div class="modal-body">
        <div class="text-center mt-3 ml-5">
          <div class="table-responsive" id="table-matkul-prasyarat">
				<table class="table table-condensed table-hover table-striped">
					<thead class="table-primary">
					<tr>
						<th>Mata Kuliah Prasyarat</th>
						<th>Nilai</th>
					</tr>
					</thead>
					<tbody>
					    {% for i,v in matkul_prasyarat.items  %}
						<tr>
						    <td>{{i}}</td>
						    <td>{{v}}</td>
						</tr>
						{% endfor %}
					</tbody>
				</table>
			</div>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
