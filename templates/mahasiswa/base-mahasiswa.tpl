{% extends 'base.tpl' %}
{% block customized_css%}
    {% load static %} 
        <link rel="stylesheet" type="text/css" href="{% static "css/tab-prima.css" %}"> 
        <link rel="stylesheet" type="text/css" href="{% static "css/navbar-prima.css" %}">  
{% endblock %}

{% block content %}
    {% include 'navbar.tpl' %}
    {% include 'predictor-tabs.tpl' %}
    {% block contentPage %}
        
    {% endblock %}
{% endblock %}
