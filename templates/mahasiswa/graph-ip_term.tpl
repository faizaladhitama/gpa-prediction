{% load static %}
    <link media="all" href="{% static 'components/nvd3/src/nv.d3.css' %}" type="text/css" rel="stylesheet" />
    <script type="text/javascript" src="{% static 'components/d3/d3.min.js' %}"></script>
    <script type="text/javascript" src="{% static 'components/nvd3/nv.d3.min.js' %}"></script>
{% load nvd3_tags %}
<head>
    {% load_chart charttype chartdata "linechart_container" True "%d %b %Y %H" %}
</head>
<body>
    {% include_container "linechart_container" 400 600 %}
</body>