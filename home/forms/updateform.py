from home.models import User
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError

class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'email',
            ]
        
        
        widgets = {
            'password': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
    

    def clean(self):
        cleaned_data = self.cleaned_data
        self.add_error(
            'first_name',
            ValidationError(
                'Campo obrigatório',
                code='required'
            )
            
        )
        self.add_error(
            'first_name',
            ValidationError(
                'Campo inválido',
                code='invalid'
            )
        )
        return super().clean()

