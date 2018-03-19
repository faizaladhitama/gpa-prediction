<title>{% block title %}Prediksi Kinerja Mahasiswa{% endblock %}</title>

{% load static %}
<script type="text/javascript" src="{% static "js/jquery-3.3.1.min.js" %}"></script>
<script type="text/javascript" scr="{% static "js/popper.min.js" %}"></script>
<link rel="stylesheet" type="text/css" href="{% static "css/bootstrap.min.css" %}">
<script type="text/javascript" src="{% static "js/bootstrap.min.js" %}"></script>
<link rel="stylesheet" type="text/css" href="{% static "css/style.css" %}"></script>

{% block customized_css%}
{% endblock %}

{% block content %}
{% endblock %}

{% load static %}
<script type="text/javascript" src="{% static " js/script.js" %}"></script>

{% block customized_js%}
{% endblock %}

<footer class="footer">
	<div class="container">
		Usagi Studio - 2018
	</div>
</footer>
