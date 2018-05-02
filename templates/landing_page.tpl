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
				<input type="submit" class="btn btn-warning font-weight-bold" id="login-button" value="Log in">
				</form>

			</div>
		</div>
</div>

<footer class="footer-copyright text-white text-center py-5" >
     © Usagi Studio - 2018
</footer>

{% endblock %}

