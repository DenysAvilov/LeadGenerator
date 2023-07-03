from .models import Form
from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import AuthenticationForm


class GeneratorForm(ModelForm):
    number = forms.ChoiceField(
        choices=[('1', '1'), ('2', '10'), ('3', '25'), ('4', '50'),
                 ('5', '100'), ('6', '250'), ('7', '500'), ('8', '1000')],
        widget=forms.Select(attrs={'class': 'form-control selected-field'}),
        help_text='Select number of leads <i class="fas fa-info-circle" '
		'data-bs-toggle="tooltip" title="Additional information"></i>.')

    class Meta:
        model = Form
        fields = ["keywords", "location", "number"]
        widgets = {
            "keywords": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Keywords"}),
            "location": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Location"}),
        }


