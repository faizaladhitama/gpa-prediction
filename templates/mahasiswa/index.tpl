{% extends 'mahasiswa/prediktor.tpl'%}
{% block contentPage %}
<h10>{% for message in messages %}
	<h3 class="messages">{{message}}</h3>
{% endfor %}</h10>
{% endblock %}


