{% extends 'mahasiswa/base-mahasiswa.tpl'%}
{% block contentPage %}
<div class="container my-5">
    <div class="row">
        <div class="col">
            <div class="col-12 mt-5">
                <h1 class="text-center search-bar">Cari Mata Kuliah</h1>
            </div>
            <form class="form-inline row" action="{% url 'mahasiswa:query-checker' %}" method="POST">
                {% csrf_token %}
                <div class="container-fluid">
                    <div class="row mt-3">
                        <input class="form-control col-4 my-2 my-sm-0 mx-auto" type="search" name="matkul" id="matkul" placeholder="Tuliskan nama mata kuliah yang akan diprediksi" aria-label="Search">
                    </div>
                <div class="row mt-3">
                    <button class="btn btn-info my-2 my-sm-0 mx-auto" type="submit">Cari <i class="fa fa-search"></i></button>
                </div>
                </div>
            </form>
        </div>
    </div>
    
</div>

{% endblock %}