{% extends 'mahasiswa/base-mahasiswa.tpl'%}
{% block contentPage %}
	<h6>
		{% for message in messages %}
			<h6 class="messages">{{message}}</h6>
		{% endfor %}
	</h6>
	{% include 'mahasiswa/predictor-tabs.tpl' %}
	{% include 'mahasiswa/detail-akademik-modal.tpl' %}
{% endblock %}
