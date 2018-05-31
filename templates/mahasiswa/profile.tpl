{% extends 'mahasiswa/base-mahasiswa.tpl' %}

{% block contentPage %}
<div class="mt-5">
    <h1 id="profile-mahasiswa-nama" class="text-center">{{name}}</h1>
</div>
<div class="table-responsive mx-auto profile-table-width">
    <table class="table mt-5 table-hover table-striped"">
        <tbody>
            <tr class="px-0" id="profile-mahasiswa-npm" class="table-light">
                <th class = "w-25" scope="row">NPM</th>
                <td>{{id}}</td>
            </tr>
            <tr class="px-0" id="profile-mahasiswa-angkatan" class="table-primary">
                <th class = "w-25" scope="row">Angkatan</th>
                <td>{{angkatan}}</td>
            </tr>
            <tr class="px-0" id="profile-mahasiswa-prodi" class="table-light">
                <th class = "w-25" scope="row">Program Studi</th>
                <td>{{prodi}}</td>
            </tr>
            <tr class="px-0" id="profile-mahasiswa-pa" class="table-primary">
                <th class = "w-25" scope="row">Pembimbing Akademis</th>
                <td>-</td>
            </tr>
            <tr class="px-0" id="profile-mahasiswa-status" class="table-light">
                <th class = "w-25" scope="row">Status Akademis</th>
                <td>{{status}}</td>
            </tr>
            <tr class="px-0" id="profile-mahasiswa-sks-lulus" class="table-primary">
                <th class = "w-25" scope="row">Total SKS Diperoleh</th>
                <td>{{sks_lulus}}</td>
            </tr>
            <tr class="px-0" id="profile-mahasiswa-mutu" class="table-light">
                <th class = "w-25" scope="row">Total Mutu</th>
                <td>{{mutu}}</td>
            </tr>
        </tbody>
    </table>
</div>
{% endblock %}