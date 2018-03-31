{% extends 'base.tpl' %}
{% block customized_css%}
<<<<<<< HEAD
<<<<<<< HEAD
{% load static %} 
<link rel="stylesheet" type="text/css" href="{% static "css/navbar-prima.css" %}">
<link rel="stylesheet" type="text/css" href="{% static "css/prediktor.css" %}">
=======
<<<<<<< HEAD
=======
>>>>>>> 10b4c1826d2f64a1b254fe830a3d10f15fd60b87
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
>>>>>>> 10b4c1826d2f64a1b254fe830a3d10f15fd60b87
{% endblock %}
{% block customized_css_content%}
{% endblock %}
{% block content %}
{% include 'navbar.tpl' %}
{% block contentPage %}
{% endblock %}
<<<<<<< HEAD
=======

{% block customized_js%}
>>>>>>> 8da698690f832436b699bb1cf30fab0273c54c6c
<<<<<<< HEAD
>>>>>>> 10b4c1826d2f64a1b254fe830a3d10f15fd60b87
=======
>>>>>>> 10b4c1826d2f64a1b254fe830a3d10f15fd60b87
{% endblock %}
