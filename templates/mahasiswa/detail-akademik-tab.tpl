<ul class="nav nav-tabs mt-5 mx-5" id="myTab" role="tablist">
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
    {% include 'mahasiswa/prediktor-evaluasi-akademik.tpl' %}  
  </div>
  <div class="tab-pane fade mx-auto" id="rekam" role="tabpanel" aria-labelledby="rekam-tab">
    {% include 'search-bar.tpl' %}
    {% include 'mahasiswa/prediktor-matkul.tpl' %}
  </div>
</div>
