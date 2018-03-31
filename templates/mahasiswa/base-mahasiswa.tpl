{% extends 'base.tpl' %}
{% block customized_css%}
    {% load static %} 
    <link rel="stylesheet" type="text/css" href="{% static "css/navbar-prima.css" %}">
{% endblock %}

{% block customized_css_content%}
{% endblock %}

{% block content %}
    {% include 'navbar.tpl' %}
    {% block contentPage %}
    {% endblock %}
{% endblock %}
