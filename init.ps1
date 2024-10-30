py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r .\requirements.txt
py .\journal_project\manage.py makemigrations
py .\journal_project\manage.py migrate
py .\journal_project\manage.py loaddata mood.json
py .\journal_project\manage.py runserver