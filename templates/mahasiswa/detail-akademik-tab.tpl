<ul class="nav nav-tabs mx-5" id="myTab" role="tablist">
  <li class="nav-item tab-head">
    <a class="nav-link active text-center" id="evaluasi-tab" data-toggle="tab" href="#peraturanAkademik" role="tab" aria-controls="peraturanAkademik" aria-selected="true"><h5>
        Peraturan <br> Akademik</h5>
    </a>
  </li>
  <li class="nav-item tab-head">
    <a class="nav-link text-center" id="matkul-tab" data-toggle="tab" href="#rekamAkademik" role="tab" aria-controls="rekamAkademik" aria-selected="false"><h5>
        Rekam <br> Akademik</h5>
    </a>
  </li>
</ul>
<div class="tab-content mx-auto" id="myTabContent2">
  <div class=" eval-content tab-pane fade show active" id="peraturanAkademik" role="tabpanel" aria-labelledby="peraturan-tab">
          <h3>Peraturan Evaluasi Akademik</h3><br>
          <h5>{{detail}}</h5><br>
          <h7>Sumber</h7><br>
          <h10>{{source}}</h10>
  </div>
  <div class="tab-pane fade mx-auto" id="rekamAkademik" role="tabpanel" aria-labelledby="rekam-tab">
         <h3>Total SKS Diperoleh</h3>
         <h5>{{all_sks}} SKS</h5>
         {% include 'mahasiswa/sks-term-table.tpl' %}
         <div class="col-xs-8">
           <h3> Riwayat IP</h3>
           {% include_container "discretebarchart_container" 400 700 %}
         </div>
  </div>
</div>
