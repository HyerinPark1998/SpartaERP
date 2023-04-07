import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pesonalassignment_01.settings")
django.setup()

from django import forms
from accounts.models import UserModel
from django.contrib.auth.forms import UserCreationForm

# form
class SignupForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2')
