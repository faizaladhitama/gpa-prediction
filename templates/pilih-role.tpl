{% extends 'base.tpl' %}
{% block customized_css%}
{% load static %} 
<link rel="stylesheet" type="text/css" href="{% static "css/pilih-role.css" %}">
{% endblock %}
{% block customized_css_content%}
{% endblock %}
{% block content %}
<div class = "container text-center mt-5">
<h2>Pilih Role</h2>
<form>
<div class="form-group row" id="pilih-role-form">
  <div class="col-10">
        <select class="form-control" id="pilihRole">
      <option>Dosen</option>
      <option>Mahasiswa</option>
    </select>
  </div>
</div>
<button type="button" class="btn btn-info pl-3 pr-3">OK</button>
</form>
</div>
{% block contentPage %}
{% endblock %}
{% endblock %}
