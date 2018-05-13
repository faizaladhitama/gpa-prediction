{% extends 'mahasiswa/base-mahasiswa.tpl'%}
{% block contentPage %}
<!-- <ul class="nav nav-tabs mx-5" id="myTab" role="tablist">
  <li class="nav-item tab-head">
    <a class="nav-link active text-center" id="evaluasi-tab" data-toggle="tab" href="#peraturanAkademik" role="tab" aria-controls="peraturanAkademik" aria-selected="true"><h5>
        Peraturan <br> Akademik</h5>
    </a>
  </li>
</ul> -->
<h3 class="text-center"> Riwayat SKS</h3>
<div class="container mx-auto my-3" id="myTabContent2">
 <div class="text-center" id="sksTerm" role="tabpanel" aria-labelledby="sks-tab">
         <h3>Total SKS Diperoleh</h3>
         <h5>{{all_sks}} SKS</h5>
         {% include 'mahasiswa/sks-term-table.tpl' %}
  </div>
  <a href="/mahasiswa" role="button" class="btn btn-info btn-arrow-left my-3">Kembali ke Prediktor</a>
</div>
{% endblock %}