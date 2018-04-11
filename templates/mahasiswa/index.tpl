<<<<<<< HEAD
{% extends 'mahasiswa/base-mahasiswa.tpl'%}
{% block contentPage %}
	<h6>
		{% for message in messages %}
			<h6 class="messages">{{message}}</h6>
		{% endfor %}
	</h6>
	{% include 'mahasiswa/prediktor.tpl' %}
	{% include 'mahasiswa/detail-akademik-modal.tpl' %}
{% endblock %}
=======
{% extends 'mahasiswa/mahasiswaBase.tpl' %}

>>>>>>> a2be2693d4b60d75bbf8816613ce9cb0607d6b80
