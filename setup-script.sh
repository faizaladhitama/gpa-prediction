#frontend
if [[ $1 == "faiz97" || $1 == "sarahdfxo" || $1 == "tinna.fauziah" ]]
then
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list
fi
apt-get update -qq && apt-get install -y -qq unzip
apt-get install -y libmemcached-dev
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
if [[ $1 == "faiz97" || $1 == "sarahdfxo" || $1 == "tinna.fauziah" ]]
then
    apt-get install -y google-chrome-stable
    apt-get install -y xvfb
    wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
fi
