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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True)

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
    preference = models.CharField(max_length=255)  # This could be a choice field or linked to another model defining the data types available

    def __str__(self):
        return f"{self.user.username}'s dashboard preferences"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dashboard_comments')
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"Comment by {self.user.username} on {self.timestamp}"

