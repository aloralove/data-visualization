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
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio', 'age', 'city', 'state', 'country', 'interests', 'first_name', 'last_name']
        
    def save(self, *args, **kwargs):
        user = super(UserProfileForm, self).save(*args, **kwargs)
        user.user.first_name = self.cleaned_data['first_name']
        user.user.last_name = self.cleaned_data['last_name']
        user.user.save()
        return user
        

from django.contrib.auth.forms import PasswordResetForm
class MyPasswordResetForm(PasswordResetForm):

    def is_valid(self):
        email = self.data['email']
        if sum([1 for u in self.get_users(email)]) == 0:
            self.add_error(None, "Unknown email; try again.")
            return False
        return super().is_valid()
    


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class SearchForm(forms.Form):
    query = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Search'}))