# insight-supply

## Project setup
### Inside a pyhton3 virtualenv run the command
```
pip install -r requirements.txt
```

### restore sqlite db from file
```
mv db.sqlite3 db.sqlite3.old
sqlite3 db.sqlite3 < db_dump.bak
```

### Create new superuser for admin access
```
python manage.py createsuperuser
```

### make db migrations after changes to models.py
```
python manage.py makemigrations <app_name> ... ie. notes
python manage.py migrate <app_name>
```

### Compiles and hot-reloads for development
```
python manage.py runserver
```

## API Examples

```
http://localhost:8000/api/v1/categories/
http://localhost:8000/api/v1/insights/
http://localhost:8000/api/v1/insights/?category=Environment
```
