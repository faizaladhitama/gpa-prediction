{% extends 'base.tpl' %}
{% block customized_css%}
{% load static %} 
<link rel="stylesheet" type="text/css" href="{% static "css/navbar.css" %}">
{% endblock %}
{% block content %}
{% include 'navbar.tpl' %}
{% endblock %}
