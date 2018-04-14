#!/bin/sh
#frontend
if [[ $1 == "faiz97" || $1 == "sarahdfxo" || $1 == "tinna.fauziah" ]]
then
	echo -e "\nRunning frontend test ....\n"
	coverage run --include='api/*','dosen/*','mahasiswa/*','sekre/*' manage.py test api.tests_selenium --failfast
	echo -e "\nFrontend test done ....\n"
fi
#backend
echo -e "\nRunning backend test ....\n"
coverage run --include='api/*','dosen/*','mahasiswa/*','sekre/*' --append manage.py test api.tests_backend dosen.tests_backend mahasiswa.tests_backend sekre.tests_backend --failfast
echo -e "\nBackend test done ....\n"
echo -e "\nGenerate coverage report ....\n"
coverage report
coverage html
