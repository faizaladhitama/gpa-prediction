{% extends 'base.tpl' %}
<<<<<<< HEAD

{% block customized_css%}
<<<<<<< HEAD
    {% load static %} 
        <link rel="stylesheet" type="text/css" href="{% static "css/tab-prima.css" %}"> 
        <link rel="stylesheet" type="text/css" href="{% static "css/navbar-prima.css" %}">  
{% endblock %}

{% block content %}
    {% include 'navbar.tpl' %}
    {% include 'predictor-tabs.tpl' %}
    {% block contentPage %}
        
    {% endblock %}
=======
	{% load static %} 
	<link rel="stylesheet" type="text/css" href="{% static "css/navbar-prima.css" %}">

	{% load static %} 
	<link rel="stylesheet" type="text/css" href="{% static "css/prediktor.css" %}">
{% endblock %}

{% block customized_css_content%}
{% endblock %}

{% block content %}
	{% include 'navbar.tpl' %}
	{% block contentPage %}
	{% endblock %}
{% endblock %}

{% block customized_js%}
>>>>>>> 8da698690f832436b699bb1cf30fab0273c54c6c
=======
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
>>>>>>> ac1e53e5d5183d390fcb3982b7fe24f1cf580fd0
{% endblock %}
