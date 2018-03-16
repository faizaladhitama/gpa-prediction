{% extends 'mahasiswa/mahasiswaBase.tpl' %}
{% block content %}
<div class = "container text-center mt-5" style="display: block;">
<h2 style="color : #09A8DD;font-weight: bold;">Pilih Role</h2>
<form>
<div class="form-group row w-50" style="margin-left: 20%;">
  <label for="example-search-input" class="col-form-label">Pilih Role : </label>
  <div class="col-10">
        <select class="form-control" id="pilihRole">
      <option>Dosen</option>
      <option>Mahasiswa</option>
    </select>
  </div>
</div>

<button type="button" class="btn btn-info pl-3 pr-3" style="background-color:#09A8DD;margin-bottom: 10%">OK</button>
</form>
</div>
{% endblock %}