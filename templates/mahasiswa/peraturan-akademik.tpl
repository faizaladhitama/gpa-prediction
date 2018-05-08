{% extends 'mahasiswa/base-mahasiswa.tpl'%}
{% block contentPage %}
<div class="eval-content tab-pane fade show active content-tab" id="peraturanAkademik" role="tabpanel" aria-labelledby="peraturan-tab">
          {% if detail != '-' %}
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
		    <a class="btn btn-link text-center" href="/mahasiswa/">
		        Kembali ke Prediktor
		    </a>
	    </div>
	</div>
{% endblock %}