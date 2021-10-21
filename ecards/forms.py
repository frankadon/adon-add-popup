from django import forms
from django import forms
from django.forms import RadioSelect, widgets, TextInput
from .models import CardData


class CardForm(forms.ModelForm):
    class Meta:
        model = CardData
        fields = [
            "business_name",
            "title",
            "greet",
            "promotion",
            "closing_statement",
            "image",
            "add_start_date",
            "add_end_date",
            "is_popup_active"
        ]
        widgets = {
            'add_start_date': TextInput(attrs={'type': 'date'}),
            'add_end_date': TextInput(attrs={'type': 'date'}),
        }
