from django import forms
from django.forms.widgets import NumberInput
import datetime
BIRTH_YEAR = ['1923','2321','1231']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class FormTesting(forms.Form):
    name =  forms.CharField(label='Simple Charfield ',initial='Kimi Ni Na Wa')
    comment = forms.CharField(widget=forms.Textarea,label='Charfield widget textarea  ')
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'rows':3}),label='Textarea with widget')
    email = forms.EmailField(label='Email Input ')
    check = forms.BooleanField(label='Check to Agree',initial=True)
    date = forms.DateField(label='Select Date ',initial= datetime.date.today)
    birthdate = forms.DateField(widget=NumberInput(attrs={'type': 'date'}),label='Date with widget')
    bith_year = forms.DateField(widget=forms.SelectDateWidget(years= BIRTH_YEAR),label='select year')
    value = forms.DecimalField(label='Enter Decimal Value')
    address = forms.CharField(required=False)
    choice = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    choice = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    
    
    
    