<ul id="mytabs" class="nav nav-justified nav-tabs">
  <li class="active prediktor-tab"><a href="#f" data-toggle="tab">Prediktor Kelulusan Evaluasi Akademik</a></li>
  <li class="prediktor-tab"><a href="#f1" data-toggle="pill">Prediktor Kelulusan Matkul</a></li>
</ul>
<div class="tab-content nav-item">
  <div id="f" class="tab-pane fade in active">
    {% include 'mahasiswa/prediktor-evaluasi-akademik.tpl' %}
  </div>
  <div id="f1" class="tab-pane fade">
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