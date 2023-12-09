# ---------------------------------------------------------------------------------------
# This code was developed with assistance from the following:
# - Django Documentation: https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/
# - Assisted by OpenAI's ChatGPT for additional guidance and debugging
#
# ----------------------------------------------------------------------------------------

from django import forms
from .models import Comment, UserProfile 
from django.contrib.auth.forms import PasswordResetForm
  
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture', 'bio')

class MyPasswordResetForm(PasswordResetForm):
   def is_valid(self):
       email = self.data["email"]
       if sum([1 for u in self.get_users(email)]) == 0:
           self.add_error(None, "Unknown email; try again")
           return False
       return super().is_valid()