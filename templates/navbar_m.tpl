<nav class="navbar navbar-expand-lg navbar-dark" style="background-color: black;">
  <a class="navbar-brand" href="#">{{user}} - {{id}}</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarText">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">{{term}}</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="#">{{role}}</a>
      </li>
      {% include 'mahasiswa/navbar-dropdown-mobile.tpl' %}
    </ul>
  </div>
</nav>