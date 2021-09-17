from django import forms
from django.forms.models import ModelForm
from .models import * 

class TeamForm(forms.ModelForm):
    class Meta:
        """Meta definition for Teamform."""

        model = Team
        fields = ('name','slug')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['slug'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'Default' , 'value':'Default'})








