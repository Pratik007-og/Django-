from django import forms
from .models import works,lives

class WorksForm(forms.ModelForm):
    class Meta:
        model = works
        fields = ["pname","cname","salary"]

class LivesForm(forms.ModelForm):
    class Meta:
        model = lives
        fields = ["pname","street","city"]