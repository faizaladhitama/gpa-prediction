{% extends 'navbar.tpl' %}

{% block navbar %}
    <a class="dropdown-item" href="/mahasiswa/profile">Profile</a>
    <div class="dropdown-divider border-info"></div>
    <a class="dropdown-item" href="#">Log Out</a>
    {% endblock %}
    
    {% block content %}
          <li class="nav-item">
        <a class="nav-link" href="/mahasiswa">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/mahasiswa/rekomendasi">Rekomendasi Matkul</a>
      </li>
    {% endblock %}
