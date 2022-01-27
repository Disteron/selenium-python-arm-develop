# Python
## Framework for AutoTests

### run pytest example:
pytest -v -m smoke
#####
pytest -v -m "not smoke"

### with allure
pytest -s -q -v -m smoke --alluredir ../reports --disable-pytest-warnings

### install requirements
pip install -r requirements.txt

### upgrade pip
pip install --upgrade pip

######
python -m venv venv
######
source venv/bin/activate
######
cd /var/lib/jenkins/workspace/$JOB_NAME/
######
deativate
######
exit
######
Для предотвращения ошибки PermissionError: [Errno 13] Permission denied
chmod +x <Путь к папке>
