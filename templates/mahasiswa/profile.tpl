{% extends 'mahasiswa/base-mahasiswa.tpl' %}

{% block contentPage %}
<div class="mt-5">
    <h1 id="profile-mahasiswa-nama" class="text-center">Profile mahasiswa</h1>
</div>
<div class="table-responsive mx-auto profile-table-width">
    <table class="table mt-5">
        <tbody>
            <tr id="profile-mahasiswa-npm" class="table-light">
                <th scope="row">NPM</th>
                <td>1506722853</td>
            </tr>
            <tr id="profile-mahasiswa-angkatan" class="table-primary">
                <th scope="row">Angkatan</th>
                <td>2015</td>
            </tr>
            <tr id="profile-mahasiswa-prodi" class="table-light">
                <th scope="row">Program Studi</th>
                <td>Ilmu Komputer, S1 Reguler</td>
            </tr>
            <tr id="profile-mahasiswa-pa" class="table-primary">
                <th scope="row">Pembimbing Akademis</th>
                <td>19839409832 - Nama PA</td>
            </tr>
            <tr id="profile-mahasiswa-status" class="table-light">
                <th scope="row">Status Akademis</th>
                <td>Aktif</td>
            </tr>
            <tr id="profile-mahasiswa-sks-lulus" class="table-primary">
                <th scope="row">Total SKS Lulus</th>
                <td>82</td>
            </tr>
            <tr id="profile-mahasiswa-mutu" class="table-light">
                <th scope="row">Total Mutu</th>
                <td>258.80</td>
            </tr>
            <tr id="profile-mahasiswa-ipk" class="table-primary">
                <th scope="row">IPK</th>
                <td>3.16</td>
            </tr>
            <tr id="profile-mahasiswa-sks-diperoleh" class="table-light">
                <th scope="row">SKS Diperoleh</th>
                <td>82</td>
            </tr>
        </tbody>
    </table>
</div>
{% endblock %}