#frontend
rm -rf .coverage
#backend
coverage run --include='api/*','mahasiswa/*' --omit='mahasiswa/utils.py','mahasiswa/views.py' manage.py test api.tests_unit api.db.tests_unit api.ml_models.tests_unit api.siak.tests_unit mahasiswa.tests_unit
#coverage run manage.py test api.db.tests_unit
coverage report -m --fail-under=90
