<nav class="navbar navbar-expand-lg navbar-dark" id = "first-navbar">
  <a class="navbar-brand" href="#">
  {% load static %} 
  <img src="{% static "assets/logo_horizontal.png" %}" width="80%" class="d-inline-block align-top" alt="">
  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse  w-100 order-3 dual-collapse2 " id="navbarNavDropdown">
    <ul class="navbar-nav ml-auto">
      <li class="nav-item">

      <span id="identity">
        <a class="nav-link activate" href="#" id = "user-term-role">
          <h10>{{name}} - {{id}}</h10><br>
          <h10>{{term}}</h10><br>
          <h10 id="role">{{role}}</h10>
        </a>
        </span>
	</li>
	<li>
        <button type="button" class="btn btn-outline-info dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" id="navbar-dropdown">
    <span class="sr-only">Toggle Dropdown</span>
  </button>
  <div class="dropdown-menu  dropdown-menu-right border-info" id = "dropdown">
    {% include 'mahasiswa/navbar-dropdown.tpl' %}
  </div>
      </li>
    </ul>
  </div>
</nav>
<nav class="navbar navbar-expand-lg" id ="second-navbar">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#underNavbar" aria-controls="underNavbar" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse  w-100 order-3 dual-collapse2 " id="underNavbar">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
    {% include 'mahasiswa/second-navbar.tpl' %}
    </ul>
  </div>
</nav>
