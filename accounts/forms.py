from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from accounts.models import User
# 
class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))

# 
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Full Name",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
    ))
    # 
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        label="Retype Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Retype Password",
                "class": "form-control"
            }
        ))
    # def clean_pass(self):
    #     pass1 = self.cleaned_data['password1']
    #     pass2 = self.cleaned_data['password2']
    #     if pass1 != pass2:
    #         raise ValidationError("Your password does not match")

        # r = requests.get(f"https://block-temporary-email.com/check/email/{email}")
        # r = r.json()
        # if r['temporary']:
        # return email
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class Change_Password_Form(forms.Form):
    password1 = forms.CharField(
    widget=forms.PasswordInput(
        attrs={
            "placeholder": "Enter Password",
            "class": "form-control"
        }
    ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter Password Again",
                "class": "form-control"
            }
        ))