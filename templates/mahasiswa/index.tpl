{% extends 'mahasiswa/base-mahasiswa.tpl' %}
{% block contentPage %}
<h10>{% for message in messages %}
	<h3 class="messages">{{message}}</h3>
{% endfor %}</h10>
{% endblock %}
{% extends 'mahasiswa/prediktor.tpl'%}

