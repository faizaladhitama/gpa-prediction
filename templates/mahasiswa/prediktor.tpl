<ul id="mytabs" class="nav nav-justified nav-tabs">
  <li class="active prediktor-tab"><a href="#evaluasi-akademik" data-toggle="tab">Prediktor Kelulusan Evaluasi Akademik</a></li>
  <li class="prediktor-tab"><a href="#kelulusan-matkul" data-toggle="pill">Prediktor Kelulusan Matkul</a></li>
</ul>
<div class="tab-content nav-item">
  <div id="evaluasi-akademik" class="tab-pane fade in active">
    {% include 'mahasiswa/prediktor-evaluasi-akademik.tpl' %}
  </div>
  <div id="kelulusan-matkul" class="tab-pane fade">
    <!-- <h3>Prediktor Kelulusan Matkul</h3>
    <p>Some content in Prediktor Kelulusan Matkul.</p> -->
	{% include 'mahasiswa/prediktor-matkul.tpl' %}
  </div>
</div>
<!-- 
{% block customized_js%}
	{% load static %}
	<script type="text/javascript" src="{% static "js/prediktor.js" %}"></script>
{% endblock %} -->