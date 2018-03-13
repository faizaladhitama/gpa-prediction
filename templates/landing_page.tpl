{% extends 'base.tpl' %}


{% block customized_css%}
{% load static %} 
<link rel="stylesheet" type="text/css" href="{% static "css/landing-page.css" %}">
{% endblock %}

{% block content %}
<div class="container-fluid">
		<div class="row ">
			<div class="col-sm-8">
				{% load static %} 
				<img id="logo" src= "{% static "assets/logo_horizontal.png" %}">
			</div>
			<div class="col-sm-4">
				<button type="button" class="btn btn-outline-warning btn-lg" id="login-button">Log in</button>
			</div>
		</div>
</div>

{% endblock %}