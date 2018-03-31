<ul class="nav nav-tabs mt-5 mx-5" id="myTab" role="tablist">
  <li class="nav-item">
    <a class="nav-link active" id="evaluasi-tab" data-toggle="tab" href="#evaluasi" role="tab" aria-controls="evaluasi" aria-selected="true">
        Prediktor <br> Lolos <br> Evaluasi Akademik
    </a>
  </li>
  <li class="nav-item">
    <a class="nav-link" id="profile-tab" data-toggle="tab" href="#matkul" role="tab" aria-controls="matkul" aria-selected="false">
        Prediktor <br> Kelulusan <br> Matkul
    </a>
  </li>
</ul>
<div class="tab-content mx-5" id="myTabContent">
  <div class="tab-pane fade show active" id="evaluasi" role="tabpanel" aria-labelledby="evaluas-tab">...</div>
  <div class="tab-pane fade" id="matkul" role="tabpanel" aria-labelledby="matkul-tab">
    {% include 'search-bar.tpl' %}
  </div>
</div>