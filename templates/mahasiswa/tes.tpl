{% extends 'navbar.tpl' %}
    {% block underNavbar %}
      <li class="nav-item">
        <a class="nav-link" href="/mahasiswa">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/mahasiswa/rekomendasi">Rekomendasi Matkul</a>
      </li>
    {% endblock %}