{% extends 'base.tpl' %}
{% block customized_css%}

{% load static %} 
<link rel="stylesheet" type="text/css" href="{% static "css/navbar-prima.css" %}">
<link rel="stylesheet" type="text/css" href="{% static "css/prediktor.css" %}">

    {% load static %} 
        <link rel="stylesheet" type="text/css" href="{% static "css/tab-prima.css" %}"> 
        <link rel="stylesheet" type="text/css" href="{% static "css/navbar-prima.css" %}">  
{% endblock %}

{% block content %}
    {% include 'navbar.tpl' %}
    {% include 'predictor-tabs.tpl' %}
    {% block contentPage %}
        
    {% endblock %}

	{% load static %} 
	<link rel="stylesheet" type="text/css" href="{% static "css/navbar-prima.css" %}">

	{% load static %} 
	<link rel="stylesheet" type="text/css" href="{% static "css/prediktor.css" %}">

{% endblock %}
{% block customized_css_content%}
{% endblock %}



{% block customized_js%}
{% endblock %}
