from django import forms

CHOICES = [('Tata','Tata'),('BMW','BMW'),('Mercedes','Mercedes'),('Audi','Audi'),('Ferrari','Ferrari'),('Hyundai','Hyundai')]

class RegForm(forms.Form):
    Manufacturer = forms.CharField(label = "Which Manufacturer?",widget = forms.Select(choices = CHOICES))
    Model = forms.CharField()
