{% extends 'mahasiswa/base-mahasiswa.tpl' %}

{% block contentPage %}
    {% load render_table from django_tables2 %}
        {% render_table table %}
{% endblock %}