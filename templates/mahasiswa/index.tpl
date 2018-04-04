<<<<<<< HEAD
{% extends 'mahasiswa/base-mahasiswa.tpl'%}
{% block contentPage %}
	<h6>
		{% for message in messages %}
			<h6 class="messages">{{message}}</h6>
		{% endfor %}
	</h6>
	{% include 'mahasiswa/prediktor.tpl' %}
=======
{% extends 'mahasiswa/base-mahasiswa.tpl' %}
{% block contentPage %}
<h10>{% for message in messages %}
	<h3 class="messages">{{message}}</h3>
{% endfor %}</h10>
>>>>>>> ac1e53e5d5183d390fcb3982b7fe24f1cf580fd0
{% endblock %}
