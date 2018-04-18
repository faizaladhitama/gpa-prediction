{% extends 'mahasiswa/base-mahasiswa.tpl' %}

{% block contentPage %}
<div class="mt-3">
    <h1 class="text-center">Profile mahasiswa</h1>
</div>
<div>
    <table class="table">
        <tbody>
            <tr>
                <th scope="row">NPM</th>
                <td>1506722853</td>
            </tr>
            <tr>
                <th scope="row">Angkatan</th>
                <td>2015</td>
            </tr>
            <tr>
                <th scope="row">Program Studi</th>
                <td>Ilmu Komputer, S1 Reguler</td>
            </tr>
            <tr>
                <th scope="row">Pembimbing Akademis</th>
                <td>19839409832 - Nama PA</td>
            </tr>
            <tr>
                <th scope="row">Status Akademis</th>
                <td>Aktif</td>
            </tr>
            <tr>
                <th scope="row">Total SKS Lulus</th>
                <td>82</td>
            </tr>
            <tr>
                <th scope="row">Total Mutu</th>
                <td>258.80</td>
            </tr>
            <tr>
                <th scope="row">IPK</th>
                <td>3.16</td>
            </tr>
            <tr>
                <th scope="row">SKS Diperoleh</th>
                <td>82</td>
            </tr>
        </tbody>
    </table>
</div>
{% endblock %}