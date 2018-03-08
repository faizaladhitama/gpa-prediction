<nav class="navbar navbar-expand-lg navbar-light" style="background-color: black;">
  <a class="navbar-brand" href="#" style="color: white">
  {% load static %} 
  <img src="{% static "assets/logo_horizontal.png" %}" width="80%" class="d-inline-block align-top" alt="">
  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse  w-100 order-3 dual-collapse2 " id="navbarNavDropdown">
    <ul class="navbar-nav ml-auto">
      <li class="nav-item">

      <div style="text-align: right;display: inline-block; margin-left: -15%;">
        <a class="nav-link activate" href="#" style="color: white;">
          <h10>Kanna</h10><br>
          <h10>2017/2018 - 2</h10><br>
          <h10">Mahasiswa</h10>
        </a>
        </div>
        {% load static %} 
        <img src="{% static "assets/profile.jpg" %}" width = "60px" class="d-inline-block align-top rounded-circle border border-white" alt="" style="margin-top: 10%; margin-left: 5%; border-width: 2px !important">
        <button type="button" class="btn btn-outline-info dropdown-toggle dropdown-toggle-split float-right" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="margin-top: 22%;">
    <span class="sr-only">Toggle Dropdown</span>
  </button>
  <div class="dropdown-menu  dropdown-menu-right border-info" style="margin-top: -1%;outline: blue">
    <a class="dropdown-item" href="/mahasiswa/profile">Profile</a>
    <div class="dropdown-divider border-info"></div>
    <a class="dropdown-item" href="#">Log Out</a>
  </div>
      </li>
    </ul>
  </div>
</nav>
<nav class="navbar navbar-expand-lg navbar-light" style="background-color: #F4D03F;box-shadow: 0px 6px 7px grey;">
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto ">
      <li class="nav-item">
        <a class="nav-link" href="/mahasiswa">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/mahasiswa/rekomendasi">Rekomendasi Matkul</a>
      </li>
    </ul>
  </div>
</nav>