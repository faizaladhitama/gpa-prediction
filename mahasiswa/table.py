import django_tables2 as tables
from mahasiswa.utils import get_global_npm, get_recommendation


class RekomendasiTable(tables.Table):
    class Meta:
        model = get_recommendation(get_global_npm())
        template_name = 'django_tables2/bootstrap4.html'
