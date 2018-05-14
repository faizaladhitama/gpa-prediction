{% extends 'mahasiswa/base-mahasiswa.tpl'%}
{% block contentPage %}
<h3 class="text-center"> Grafik IP</h3>
<div class="container mx-auto my-3" id="myTabContent2">
 <div class="col-xs-8">
           {% include_container "discretebarchart_container" 400 1000 %}
 </div>
  <div class="row ">
	    <div class="col ">
  			<a href="/mahasiswa" role="button" class="btn btn-info btn-arrow-left my-3">Kembali ke Prediktor</a>
  			<a href="/mahasiswa/peraturan-akademik" role="button" class="btn btn-danger btn-arrow-left my-3">
  			Peraturan Akademik</a>
  			<a href="/mahasiswa/riwayat-sks" role="button" class="btn btn-warning btn-arrow-left my-3">Riwayat SKS</a>
	    </div>
	</div>
</div>
 {% load nvd3_tags %}
 {% load_chart charttype chartdata "discretebarchart_container" %}
{% endblock %}