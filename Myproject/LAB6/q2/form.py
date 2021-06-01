from django import forms
CHOICES = [('Maths','Maths'),('English','Engish'),('Physics','Physics'),('Chemistry','Chemistry')]
class my_form(forms.Form):
    name = forms.CharField()
    roll_no = forms.CharField()
    subject = forms.CharField(label = "Subject: ",widget = forms.Select(choices = CHOICES))