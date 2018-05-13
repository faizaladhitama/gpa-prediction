#frontend
rm -rf .coverage
if [[ $1 == "faiz97" || $1 == "sarahdfxo" || $1 == "tinna.fauziah" ]]
then
	coverage run --include='api/*','mahasiswa/*' manage.py test api.tests_functional
fi
#backend
coverage run --include='api/*','mahasiswa/*' --append manage.py test api.tests_unit api.db.tests_unit api.siak.tests_unit mahasiswa.tests_unit
coverage report -m --fail-under=90
