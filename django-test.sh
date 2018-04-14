#frontend
if [[ $1 == "faiz97" || $1 == "sarahdfxo" || $1 == "tinna.fauziah" ]]
then
	echo -e "\nRunning functional tests ....\n"
	coverage run --include='api/*','mahasiswa/*' manage.py test api.tests_functional --failfast
	echo -e "\nFunctional tests done ....\n"
fi
#backend
echo -e "\nRunning unit tests ....\n"

coverage run --include='api/*','mahasiswa/*' --append manage.py test api.tests_unit api.db.tests_unit api.siak.tests_unit mahasiswa.tests_unit --failfast
echo -e "\nUnit tests done ....\n"
echo -e "\nGenerate coverage report ....\n"
coverage report
coverage html
