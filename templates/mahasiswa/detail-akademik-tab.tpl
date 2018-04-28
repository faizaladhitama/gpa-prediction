{% extends 'mahasiswa/base-mahasiswa.tpl'%}
{% block contentPage %}
<ul class="nav nav-tabs mx-5" id="myTab" role="tablist">
  <li class="nav-item tab-head">
    <a class="nav-link active text-center" id="evaluasi-tab" data-toggle="tab" href="#peraturanAkademik" role="tab" aria-controls="peraturanAkademik" aria-selected="true"><h5>
        Peraturan <br> Akademik</h5>
    </a>
  </li>
  <li class="nav-item tab-head">
    <a class="nav-link text-center" id="matkul-tab" data-toggle="tab" href="#sksTerm" role="tab" aria-controls="rekamAkademik" aria-selected="false"><h5>
        Riwayat <br> SKS</h5>
    </a>
  </li>
    <li class="nav-item tab-head">
    <a class="nav-link text-center" id="matkul-tab" data-toggle="tab" href="#grafikIp" role="tab" aria-controls="rekamAkademik" aria-selected="false"><h5>
        Riwayat <br> IP</h5>
    </a>
  </li>
</ul>
<div class="tab-content mx-auto" id="myTabContent2">
  <div class="eval-content tab-pane fade show active content-tab" id="peraturanAkademik" role="tabpanel" aria-labelledby="peraturan-tab">
          {% if detail != '-' %}
          <h4>
          Anda berada pada <strong> semester {{semester_now}} </strong>
          dengan total sks yang anda diperoleh sebanyak <strong>{{all_sks}} sks</strong>.
          Anda membutuhkan <strong>{{sks_kurang}} sks</strong>
          untuk dapat lolos evaluasi akademik di <strong> semester {{semsester_evaluation}}</strong>.
          Semangat! Dengan usaha yang maksimal anda pasti bisa lolos evaluasi akademik! :)
          </h4>
          {% endif %}
          <h7><strong>Peraturan Evaluasi Akademik</strong></h7><br>
          <h10>{{detail}}</h10><br>
          <h7>Sumber</h7><br>
          <h10>{{source}}</h10>
  </div>
  <div class="tab-pane fade mx-auto content-tab" id="sksTerm" role="tabpanel" aria-labelledby="sks-tab">
         <h3>Total SKS Diperoleh</h3>
         <h5>{{all_sks}} SKS</h5>
         {% include 'mahasiswa/sks-term-table.tpl' %}
  </div>
    <div class="tab-pane fade mx-auto" id="grafikIp" role="tabpanel" aria-labelledby="ip-tab">
         <div class="col-xs-8">
           {% include_container "discretebarchart_container" 400 1000 %}
         </div>
  </div>
</div>
{% load nvd3_tags %}
    {% load_chart charttype chartdata "discretebarchart_container" %}
    <div class="row ">
	    <div class="col ">
		    <button type="button" class="btn btn-link text-center" data-toggle="modal" href="/mahasiswa/">
		        Kembali ke Prediktor
		    </button>
	    </div>
	</div>
{% endblock %}