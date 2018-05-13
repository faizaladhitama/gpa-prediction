{% extends 'mahasiswa/base-mahasiswa.tpl'%}
{% block contentPage %}
	<div>
		{% for message in messages %}
			<div class="alert alert-success h6">
				<button type="button" class="close" data-dismiss="alert" aria-label="Close">
   					<span aria-hidden="true">&times;</span>
  				</button>
				{{message}}
			</div>
		{% endfor %}
	</div>
	{% include 'mahasiswa/predictor-tabs.tpl' %}
{% endblock %}
{% block modal%}
{% include 'mahasiswa/detail-akademik-modal.tpl' %}
{% endblock%}
