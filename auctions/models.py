from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



# DONT FORGET TO MIGRATE AFTER CREATING THIS MODEL
# run to migrate changes to database:
#
# > python manage.py makemigrations
# > python manage.py migrate
#


class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    profile_picture = models.ImageField(upload_to='profile_pictures/%Y/%m/%d/', blank=True, null=True)
    bio = models.TextField(blank=True)
    age = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    interests = models.TextField(blank=True)
    

    def __str__(self):
        return f"{self.user.username}'s profile"

#allows users to store their own city preferences for the dashboard
class UserCityPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='city_preferences')
    city_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username}'s city preference is {self.city_name}"

class DashboardPreferences(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dashboard_preferences')
    preference = models.CharField(max_length=255)  

    def __str__(self):
        return f"{self.user.username}'s dashboard preferences"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dashboard_comments')
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    chart_id = models.CharField(max_length=100, default='default_chart_id') 

    def __str__(self):
        return f"Comment by {self.user.username} on {self.timestamp}"

