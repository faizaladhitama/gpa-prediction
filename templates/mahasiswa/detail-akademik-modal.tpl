  <div class="modal fade" id="detailAkademik">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
            <h4 class="modal-title">Detail Akademik Mahasiswa</h4>
            <button type="button" class="close" data-dismiss="modal">&times;</button>
        </div>
      <div class="modal-body">
        {% include 'mahasiswa/detail-akademik-tab.tpl' %}
        {% include_container "linechart_container" 400 600 %}
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
