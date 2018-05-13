{% extends 'base.tpl' %}
{% block customized_css%}
	{% load static %} 
	<link rel="stylesheet" type="text/css" href="{% static "css/navbar-prima.css" %}">
	<link rel="stylesheet" type="text/css" href="{% static "css/prediktor.css" %}">
	<link rel="stylesheet" type="text/css" href="{% static "css/mahasiswa-profile.css" %}">
	<link rel="stylesheet" type="text/css" href="{% static "css/button.css" %}">
	<link rel="stylesheet" type="text/css" href="{% static "css/tab-prima.css" %}">
	<link rel="stylesheet" type="text/css" href="{% static "css/navbar-prima.css" %}">
		<link rel="stylesheet" type="text/css" href="{% static "css/detail-akademik.css" %}">
{% endblock %}
{% block customized_css_content%}
{% endblock %}
{% block content %}
	{% include 'navbar.tpl' %}
	{% block contentPage %}
	{% endblock %}
	<footer class="footer-copyright text-center" >
    	© Usagi Studio - 2018
	</footer>
	{% block modal %}
    {% endblock %}
{% endblock %}
