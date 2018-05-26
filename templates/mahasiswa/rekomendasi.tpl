{% extends 'mahasiswa/base-mahasiswa.tpl' %}
{% block contentPage %}
<div class="container mx-auto my-3" id="myTabContent2">
	<div class="col-xs-8 mt-5">
	        <h4 class="font-weight-bold">Rekomendasi Mata Kuliah</h4>
	        {% if table.object_list|length != 0 %}
		    <div class="table-responsive" id="rekomendasi-table">
				<table class="table table-condensed table-hover table-striped">
					<thead class="table-primary">
						<tr>
							<th>Kode Mata Kuliah</th>
							<th>Nama Mata Kuliah</th>
						</tr>
					</thead>
					<tbody>
					    {% for prediksi in table %}
					    <tr>
					    {% for record in prediksi %}
					    <td>{{ record }}</td>
					    {% endfor %}
					    </tr>
					    {% endfor %}
					</tbody>
			    </table>
			    {% if table.has_other_pages %}
			    <ul class="pagination">
			    {% if table.has_previous %}
			    <li class="page-item"><a class="page-link" href="?page={{ table.previous_page_number }}">&laquo;</a></li>
			    {% else %}
			    <li class="page-item disabled"><a class="page-link" href="#">&laquo;</a></li>
			    {% endif %}
			    {% for i in table.paginator.page_range %}
			    {% if table.number == i %}
			    <li class="page-item active"><a class="page-link" href="#">{{ i }}</a></li>
      {% else %}
        <li class="page-item"><a class="page-link" href="?page={{ i }}">{{ i }}</a></li>
      {% endif %}
    {% endfor %}
    {% if table.has_next %}
      <li class="page-item"><a class="page-link" href="?page={{ table.next_page_number }}">&raquo;</a></li>
    {% else %}
      <li class="page-item disabled"><a class="page-link" href="#">&raquo;</a></li>
    {% endif %}
  </ul>
{% endif %}
    {% else %}
        <div class="alert alert-danger">
    <strong>Mohon Maaf</strong> Belum ada mata kuliah yang direkomendasikan.
  </div>
    {% endif %}
			</div>
	</div>
</div>
{% endblock %}