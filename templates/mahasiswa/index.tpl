{% extends 'mahasiswa/base-mahasiswa.tpl'%}
{% block contentPage %}
	{% include 'mahasiswa/prediktor.tpl' %}
	<h6>{% for message in messages %}
	<h6 class="messages">{{message}}</h6>
{% endfor %}</h6>

{% endblock %}
