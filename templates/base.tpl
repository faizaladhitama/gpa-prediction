<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{% block title %}Prediksi Kinerja Mahasiswa{% endblock %}</title>
{% load static %}
<link media="all" href="{% static 'components/nvd3/src/nv.d3.css' %}" type="text/css" rel="stylesheet" />
<script type="text/javascript" src="{% static 'components/d3/d3.min.js' %}"></script>
<script type="text/javascript" src="{% static 'components/nvd3/nv.d3.js' %}"></script>
<script type="text/javascript" src="{% static 'js/jquery-3.3.1.min.js' %}"></script>
<script type="text/javascript" src="{% static 'js/popper.min.js' %}"></script>
<link rel="stylesheet" type="text/css" href="{% static 'css/bootstrap.min.css' %}">
<script type="text/javascript" src="{% static 'js/bootstrap.min.js' %}"></script>
<link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
<link rel="apple-touch-icon" sizes="57x57" href="{% static 'favicon/apple-icon-57x57.png' %}">
<link rel="apple-touch-icon" sizes="60x60" href="{% static 'favicon/apple-icon-60x60.png' %}">
<link rel="apple-touch-icon" sizes="72x72" href="{% static 'favicon/apple-icon-72x72.png' %}">
<link rel="apple-touch-icon" sizes="76x76" href="{% static 'favicon/apple-icon-76x76.png' %}">
<link rel="apple-touch-icon" sizes="114x114" href="{% static 'favicon/apple-icon-114x114.png' %}">
<link rel="apple-touch-icon" sizes="120x120" href="{% static 'favicon/apple-icon-120x120.png' %}">
<link rel="apple-touch-icon" sizes="144x144" href="{% static 'favicon/apple-icon-144x144.png' %}">
<link rel="apple-touch-icon" sizes="152x152" href="{% static 'favicon/apple-icon-152x152.png' %}">
<link rel="apple-touch-icon" sizes="180x180" href="{% static 'favicon/apple-icon-180x180.png' %}">
<link rel="icon" type="image/png" sizes="192x192" href="{% static 'favicon/android-icon-192x192.png' %}">
<link rel="icon" type="image/png" sizes="32x32" href="{% static 'favicon/favicon-32x32.png' %}">
<link rel="icon" type="image/png" sizes="96x96" href="{% static 'favicon/favicon-96x96.png' %}">
<link rel="icon" type="image/png" sizes="16x16" href="{% static 'favicon/favicon-16x16.png' %}">
<link rel="manifest" href="{% static 'favicon/manifest.json' %}">
<meta name="msapplication-TileColor" content="#ffffff">
<meta name="msapplication-TileImage" content="/ms-icon-144x144.png">
<meta name="theme-color" content="#ffffff">

{% block customized_css%}
{% endblock %}

<div id="loader">
	{% load static %}
	<img src="{% static 'assets/loader.gif' %}" id="img-loader" >
	<p>please wait ;)</p>
</div>

{% block content %}
{% endblock %}

{% load static %}
<script type="text/javascript" src="{% static 'js/script.js' %}"></script>
