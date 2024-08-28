from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UpdateOrCreateForm(UserCreationForm):

    def __init__(
                self, 
                *args: Any, 
                matricula: Any =None, 
                first_name: Any =None,
                last_name: Any =None,
                email: Any =None,
                **kwargs: Any, 
                ):
        super(UpdateOrCreateForm, self).__init__(*args, **kwargs)
        if matricula:
            self.fields['username'].initial = matricula
        if first_name:
            self.fields['first_name'].initial = first_name
        if last_name:
            self.fields['last_name'].initial = last_name
        if email:
            self.fields['email'].initial = email
    


    class Meta:
        model = User
        fields = [
            'username',
            'first_name', 
            'last_name', 
            'email',
            ]
        
        
        widgets = {
            'first_name': forms.TextInput(
                attrs = {
                    'class': 'form-cadastro',
                    'required': 'required',
                },
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': 'form-cadastro',
                    'required': 'required',

                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-cadastro',
                    'required': 'required',

                }

            ),
        }
    
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'readonly': 'readonly',
                'class': 'form-cadastro'
            }
        ),
    )

    password1 = forms.CharField(
        label = 'senha',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-cadastro'
            }
        ),      
        help_text=[
            'Sua senha deve conter pelo menos 8 caracteres',
            'Sua senha não pode ser inteiramente numérica',
            'Sua senha não pode ser comum (óbvia)',

        ]
    )
    
    password2 = forms.CharField(
        label = 'confirma senha',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-cadastro'
            }
        ),
        help_text=[
            'Digite a mesma senha que foi digitada anteriormente',
        ],
    )
"""
    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if len(password) < 8:
            msg = ValidationError(
                'A senha deve conter pelo menos 8 caracteres',
                code = 'invalid',
                )
            self.add_error('password', msg)
        if str(password).isnumeric():
            msg = ValidationError(
                'A senha não pode ser inteiramente numérica',
                code = 'invalid',
                )
            self.add_error('password', msg)
        if password.isalpha():
            msg = ValidationError(
                'A senha não pode ser inteiramente alfabética',
                code = 'invalid',
                )
            self.add_error('password', msg)
        print(password, password2)
        if password != password2:
            msg = ValidationError(
                'As senhas devem ser congruentes',
                code = 'invalid',
                )
            self.add_error('password', msg)
            self.add_error('password2', msg)
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if first_name and last_name:
            if first_name == last_name:
                msg = ValidationError(
                    'primeiro nome não pode ser igual ao último nome',
                    code = 'invalid',
                    )
                self.add_error('first_name', msg)
                self.add_error('last_name', msg)
        else:
            if first_name == '':
                msg = ValidationError(
                    'primeiro nome não pode ser vazio',
                    code = 'invalid',
                    )
                self.add_error('first_name', msg)
            
            if last_name == '':
                msg = ValidationError(
                    'último nome não pode ser vazio',
                    code = 'invalid',
                    )
                self.add_error('last_name', msg)
        return super().clean()
"""
