from django import forms
from .models import *


class StringForm(forms.ModelForm):

    class Meta:
        model = String
        exclude = [""]
