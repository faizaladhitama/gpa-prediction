#frontend
apt-get update -qq && apt-get install -y -qq unzip
apt-get install -y apt-utils && apt-get install -y libmemcached-dev
pip install -r requirements.txt
chmod +x deployment.sh
./deployment.sh