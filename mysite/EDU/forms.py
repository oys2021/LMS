from dataclasses import fields
from django.forms import ModelForm
from EDU.models import *

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        exclude=['user']
