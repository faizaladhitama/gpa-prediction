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
				<img id="logo" src= "{% static "assets/logo_persegi.png" %}">
			</div>
			<div class="col-sm-4">
				<form class="login-form">
					<div class="form-group">
						<label for="username">Username</label>
						<input type="text" name="username" id="username" class="form-group">
					</div>
					<div class="form-group">
						<label for="username">Password </label>
						<input type="text" name="username" id="username" class="form-group">
					</div>
				<button type="button" class="btn btn-outline-warning" id="login-button">Log in</button>
				</form>

			</div>
		</div>
</div>

{% endblock %}