<div class="container">
  <button type="button" class="btn btn-link" data-toggle="modal" data-target="#detailAkademik">
    Lihat Selengkapnya
  </button>
  <div class="modal fade" id="detailAkademik">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
            <h4 class="modal-title">Detail Akademik Mahasiswa</h4>
            <button type="button" class="close" data-dismiss="modal">&times;</button>
        </div>
      <div class="modal-body">
        {% include 'mahasiswa/detail-akademik-tab.tpl' %}
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>

</div>
