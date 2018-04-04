{% extends 'index.tpl' %}

{% block title %} Prediktor Kelulusan Evaluasi Akademik{% endblock %}

{% block content %}
<div class="container-fluid">
		<div class="row ">
			<div class="col">
				{% load static %} 
				<img src= "{% static "assets/greenButton.png" %}">
			</div>
		</div>

		<div class="row ">
			<div class="col">
				Selamat, anda berpeluang lolos evaluasi akademik semester 2!
			</div>
		</div>
</div>
{% endblock %}

