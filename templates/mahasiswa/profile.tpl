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
                <td></td>
            </tr>
            <tr>
                <th scope="row">Angkatan</th>
                <td></td>
            </tr>
            <tr>
                <th scope="row">Program Studi</th>
                <td></td>
            </tr>
            <tr>
                <th scope="row">Pembimbing Akademis</th>
                <td></td>
            </tr>
            <tr>
                <th scope="row">Status Akademis</th>
                <td></td>
            </tr>
            <tr>
                <th scope="row">Total SKS Lulus</th>
                <td></td>
            </tr>
            <tr>
                <th scope="row">Total Mutu</th>
                <td></td>
            </tr>
            <tr>
                <th scope="row">IPK</th>
                <td></td>
            </tr>
            <tr>
                <th scope="row">SKS Diperoleh</th>
                <td></td>
            </tr>
        </tbody>
    </table>
</div>
{% endblock %}