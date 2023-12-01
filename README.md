# Final Project 

python -m venv venv 



.\venv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
*optional* python manage.py createsuperuser
python manage.py runserver

*optional- create custom query objects* python manage.py shell

WHEN DONE WITH VENV
deactivate




Docker for deployment
```
create image
docker build -t my-django-app .

run image (create container)
docker run -p 8000:8000 -e PORT=8000 my-django-app



Depoly app to google cloud App Engine
docker tag my-django-app gcr.io/gcp_project_id/my-django-app
docker push gcr.io/gcp_project_id/my-django-app

gcloud app deploy


```

main is production 

master is dev