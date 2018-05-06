{% extends 'mahasiswa/base-mahasiswa.tpl'%}
{% block contentPage %}
<!-- <ul class="nav nav-tabs mx-5" id="myTab" role="tablist">
  <li class="nav-item tab-head">
    <a class="nav-link active text-center" id="evaluasi-tab" data-toggle="tab" href="#peraturanAkademik" role="tab" aria-controls="peraturanAkademik" aria-selected="true"><h5>
        Peraturan <br> Akademik</h5>
    </a>
  </li>
</ul> -->
<h3 class="text-center"> Grafik IP</h3>
<div class="container mx-auto my-3" id="myTabContent2">
  <div class="text-center " id="grafikIp" aria-labelledby="ip-tab">
    <div class="col-xs-8">
      {% include_container "discretebarchart_container" 400 1000 %}
    </div>
  </div>
</div>
{% load nvd3_tags %}
    {% load_chart charttype chartdata "discretebarchart_container" %}
  <a href="/mahasiswa" role="button" class="btn btn-info btn-arrow-left my-3">Kembali ke Prediktor</a>
</div>
{% endblock %}