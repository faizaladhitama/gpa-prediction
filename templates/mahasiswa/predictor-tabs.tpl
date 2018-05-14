<ul class="nav nav-tabs mt-5 mx-5" id="myTab" role="tablist">
  <li class="nav-item tab-head" id="tab-prediktor-evaluasi-akademik">
    <a class="nav-link active text-center" id="evaluasi-tab" data-toggle="tab" href="#evaluasi" role="tab" aria-controls="evaluasi" aria-selected="true"><h5>
        Prediktor Kelulusan <br> Evaluasi Akademik</h5>
    </a>
  </li>
  <li class="nav-item tab-head" id="tab-prediktor-matkul">
    <a class="nav-link text-center" id="matkul-tab" data-toggle="tab" href="#matkul" role="tab" aria-controls="matkul" aria-selected="false"><h5>
        Prediktor Kelulusan <br> Mata Kuliah</h5>
    </a>
  </li>
</ul>
<div class="tab-content mx-auto" id="myTabContent">
  <div class=" eval-content tab-pane fade show active" id="evaluasi" role="tabpanel" aria-labelledby="evaluas-tab">
    {% include 'mahasiswa/prediktor_evaluasi_akademik.tpl' %}
  </div>
  <div class="tab-pane fade mx-auto" id="matkul" role="tabpanel" aria-labelledby="matkul-tab">
    {% include 'mahasiswa/prediktor-matkul.tpl' %}
  </div>
</div>