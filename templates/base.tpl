<title>{% block title %}Prediksi Kinerja Mahasiswa{% endblock %}</title>

{% load static %} 
<link rel="stylesheet" type="text/js" href="{% static "js/jquery-3.3.1.min.js" %}">
<link rel="stylesheet" type="text/js" href="{% static "js/popper.min.js" %}">
<link rel="stylesheet" type="text/css" href="{% static "css/bootstrap.min.css" %}">
<link rel="stylesheet" type="text/js" href="{% static "js/bootstrap.min.js" %}">
<link rel="stylesheet" type="text/css" href="{% static "css/style.css" %}">

{% block customized_css%}
{% endblock %}

{% block content %}
{% endblock %}

{% load static %} 
<script type="text/javascript" src= "{% static "js/script.js" %}"></script>

{% block customized_js%}
{% endblock %}

<footer class="footer">
	<div class="container">
		Usagi Studio - 2018
	</div>
</footer>
