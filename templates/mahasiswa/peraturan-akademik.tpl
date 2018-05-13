{% extends 'mahasiswa/base-mahasiswa.tpl'%}
{% block contentPage %}
<h3 class="text-center"> Peraturan Akademik</h3>
<div class="container">
  <div class="container mx-auto" id="peraturanAkademik" role="tabpanel" aria-labelledby="peraturan-tab">
       {% if detail != '-' %}
       <div class="mx-auto my-3 text-center">
         <img src="https://memegenerator.net/img/instances/59493154.jpg"  />
       </div>
       <h4>
       Anda berada pada <strong> semester {{semester_now}} </strong>
       dengan total sks yang anda diperoleh sebanyak <strong>{{all_sks}} sks</strong>.
       Anda membutuhkan <strong>{{sks_kurang}} sks</strong>
       untuk dapat lolos evaluasi akademik di <strong> semester {{semester_evaluation}}</strong>.
       Semangat! Dengan usaha yang maksimal anda pasti bisa lolos evaluasi akademik! :)
       </h4>
       <h7><strong>Peraturan Evaluasi Akademik</strong></h7><br>
       <h10>{{detail}}</h10><br>
       <h7>Sumber</h7><br>
       <h10>{{source}}</h10>
       {% else %}
       <div class="mx-auto my-3 text-center">
         <img src="http://i.pokeme.com/meme/img/00cx.jpg" />
       </div>
       <h4>
       Anda berada pada <strong> semester {{semester_now}} </strong>
       dengan total sks yang anda diperoleh sebanyak <strong>{{all_sks}} sks</strong>.
       Anda sudah lolos evaluasi akademik di <strong> semester {{semester_evaluation}}</strong>.
       Pertahankan! :)
       </h4>
       {% endif %}
  </div>
  <div class="row ">
           <div class="col ">
                  <a href="/mahasiswa" role="button" class="btn btn-info btn-arrow-left my-3 ml-3">Kembali ke Prediktor</a>
                  <a href="/mahasiswa/riwayat-sks" role="button" class="btn btn-warning btn-arrow-left my-3 ml-3">Riwayat SKS</a>
                  <a href="/mahasiswa/riwayat-ip" role="button" class="btn btn-success btn-arrow-left my-3 ml-3">Riwayat IP</a>
           </div>
  </div>
</div>
{% endblock %}
