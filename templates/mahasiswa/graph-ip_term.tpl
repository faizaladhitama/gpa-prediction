{% extends 'mahasiswa/base-mahasiswa.tpl'%}
{% block contentPage %}
 <div class="col-xs-8">
           {% include_container "discretebarchart_container" 400 1000 %}
 </div>
  <div class="row ">
	    <div class="col ">
		    <a class="btn btn-link text-center" href="/mahasiswa/">
		        Kembali ke Prediktor
		    </a>
	    </div>
	</div>
 {% load nvd3_tags %}
 {% load_chart charttype chartdata "discretebarchart_container" %}
{% endblock %}