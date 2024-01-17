# CRYPTOCURRENCY API
djangorestframework + bs4 + celery


## Start
dependencies:
```python3 -m pip3 install -r requirements.txt```

migrations + runserver:

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserve
```

celery command:
```celery -A crypto_tracker worker -l info```
