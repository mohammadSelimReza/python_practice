from django import forms
from .models import CharacterModel

class CharacterForm(forms.ModelForm):
    class Meta:
        model = CharacterModel
        fields = '__all__'