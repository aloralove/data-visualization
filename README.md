# Data Visualization

## Setting Up the Development Environment

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
# optional
python manage.py createsuperuser
python manage.py runserver

# optional - create custom query objects
python manage.py shell

# When done with venv
deactivate

```
## Docker For Development
```bash
# Create image
docker build -t my-django-app .

# Run image (create container)
docker run -p 8000:8000 -e PORT=8000 my-django-app

```
## Deployment Google Cloud App Engine (Manually)
```bash
# Tag the Docker image
docker tag my-django-app gcr.io/sodium-airport-395522/my-django-app

# Push the image to Google Container Registry
docker push gcr.io/sodium-airport-395522/my-django-app

# Deploy the app
gcloud app deploy
```
