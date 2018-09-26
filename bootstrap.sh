virtualenv -p python3 venv
. venv/bin/activate
pip install 'git+https://github.com/zalando/connexion.git@dev-2.0#egg=connexion[swagger-ui]'
