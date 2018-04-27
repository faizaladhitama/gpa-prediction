{% extends 'mahasiswa/base-mahasiswa.tpl' %}

{% block contentPage %}
<div class="mt-5">
    <h1 id="profile-mahasiswa-nama" class="text-center">{{data_mahasiswa.nama}}</h1>
</div>
<div class="table-responsive mx-auto profile-table-width">
    <table class="table mt-5">
        <tbody>
            <tr id="profile-mahasiswa-npm" class="table-light">
                <th scope="row">NPM</th>
                <td>{{data_mahasiswa.npm}}</td>
            </tr>
            <tr id="profile-mahasiswa-angkatan" class="table-primary">
                <th scope="row">Angkatan</th>
                <td>{{data_mahasiswa.angkatan}}</td>
            </tr>
            <tr id="profile-mahasiswa-prodi" class="table-light">
                <th scope="row">Program Studi</th>
                <td>{{data_mahasiswa.prodi}}</td>
            </tr>
            <tr id="profile-mahasiswa-pa" class="table-primary">
                <th scope="row">Pembimbing Akademis</th>
                <td>-</td>
            </tr>
            <tr id="profile-mahasiswa-status" class="table-light">
                <th scope="row">Status Akademis</th>
                <td>{{data_mahasiswa.status}}</td>
            </tr>
            <tr id="profile-mahasiswa-sks-lulus" class="table-primary">
                <th scope="row">Total SKS Lulus</th>
                <td>{{data_mahasiswa.sks_lulus}}</td>
            </tr>
            <tr id="profile-mahasiswa-mutu" class="table-light">
                <th scope="row">Total Mutu</th>
                <td>{{data_mahasiswa.mutu}}</td>
            </tr>
            <tr id="profile-mahasiswa-ipk" class="table-primary">
                <th scope="row">IPK</th>
                <td>3.16</td>
            </tr>
            <tr id="profile-mahasiswa-sks-diperoleh" class="table-light">
                <th scope="row">SKS Diperoleh</th>
                <td>{{data_mahasiswa.sks_diperoleh}}</td>
            </tr>
        </tbody>
    </table>
</div>
{% endblock %}