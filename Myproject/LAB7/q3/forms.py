from django import forms
from .models import author,publisher,book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = author
        fields = ["fname","lname","email"]

class PublisherForm(forms.ModelForm):
    class Meta:
        model = publisher
        fields = ["name","street","city","state","country","website"]

class BookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ["title","publish_date"]