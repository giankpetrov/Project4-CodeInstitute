from django import forms
from django.forms impor ModelForm
from .models import Users

# Create a new user
class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ('Name', 'Email', 'Password')