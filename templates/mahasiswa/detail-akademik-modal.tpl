  <div class="modal fade" id="detailAkademik">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
            <h4 class="modal-title">Detail Akademik Mahasiswa</h4>
            <button type="button" class="close" data-dismiss="modal">&times;</button>
        </div>
      <div class="modal-body">
<!--         {% include 'mahasiswa/detail-akademik-tab.tpl' %} -->
        <h5 class="text-center">Tekan tombol di bawah ini untuk melihat detail akademik</h5>
        <div class="text-center mt-3">
          <a href="/mahasiswa/peraturan-akademik" role="button" class="btn btn-danger btn-arrow-right" onclick="displayLoader()">Peraturan Akademik</a>
          <a href="/mahasiswa/riwayat-sks" role="button" class="btn btn-warning btn-arrow-right" onclick="displayLoader()">Riwayat SKS</a>
          <a href="/mahasiswa/riwayat-ip" role="button" class="btn btn-success btn-arrow-right" onclick="displayLoader()">Riwayat IP</a>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
