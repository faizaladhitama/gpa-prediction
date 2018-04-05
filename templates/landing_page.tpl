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
				{% for message in messages %}
				<h3 class="messages">{{message}}</h3>
				{% endfor %}
				<form class="login-form" action="{% url 'api:auth-login' %}" method="POST">                
                {% csrf_token %}
					<div class="form-group">
						<label for="username" class="login-label">Username</label>
						<input type="text" name="username" id="username" class="form-control" onfocus="deleteMessage()">
					</div>
					<div class="form-group">
						<label for="password" class="login-label">Password </label>
						<input type="password" name="password" id="password" class="form-control" onfocus="deleteMessage()">
					</div>
				<input type="submit" class="btn btn-outline-warning" id="login-button" value="Log in">
				</form>

			</div>
		</div>
</div>

{% endblock %}