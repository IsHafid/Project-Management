from django import forms
from django.forms import fields
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.core.exceptions import ValidationError
class SignupForm(forms.ModelForm):
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm your password', widget=forms.PasswordInput)
    class Meta:
    
        """Meta definition for Signupform."""

        model = UsersBase
        exclude = ['is_active','updated','created']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['statut'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['firstname'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'firstname'})
        self.fields['lastname'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'lastname'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'email'})
        self.fields['img'].widget.attrs.update(
            {'class': 'form-control rounded-pill', 'placeholder': 'img'})
        self.fields['slug'].widget.attrs.update(
            {'class': 'form-control rounded-pill', 'placeholder': 'slug' , 'value':'Default'})
        self.fields['phonenum'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': '06xxxxxxxx' })
        self.fields['CIN'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'CIN'})
        self.fields['birthdate'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'birthdate'})
        self.fields['cv'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['img'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['team'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control rounded-pill', 'placeholder': 'Repeat Password'})

    def verf_CIN(self):
        CIN = self.cleaned_data['CIN'].lower()
        fn= UsersBase.objects.filter(CIN=CIN)
        if fn.count():
            raise forms.ValidationError("CIN already exists")
        return CIN

    def verf_phonenum(self):
        phonenum = self.cleaned_data['phonenum']
        fn= UsersBase.objects.filter(phonenum=phonenum)
        if fn.count():
            raise forms.ValidationError("phonenum already exists")
        return phonenum
        
    def verf_pswrd2(self):
        cl_dt = self.cleaned_data
        if cl_dt['password'] != cl_dt['password2']:
          raise forms.ValidationError('Passwords do not match ')
        return cl_dt['password2']

    def Verifyemail(self):
        email = self.cleaned_data['email'].lower()
        if UsersBase.objects.filter(email=email).exists():
            raise forms.ValidationError('Please use another Email, Email already exists')
        return email

class UpdateForm(forms.ModelForm):
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm your password', widget=forms.PasswordInput)
    class Meta:
    
        """Meta definition for Signupform."""
        
        model = UsersBase
        exclude = ['updated','created']


            
    def __init__(self, *args, **kwargs,):
        super().__init__(*args, **kwargs)
        
        self.fields['statut'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['firstname'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'firstname'})
        self.fields['lastname'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'lastname'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'email'})
        self.fields['img'].widget.attrs.update(
            {'class': 'form-control rounded-pill', 'placeholder': 'img'})
        self.fields['slug'].widget.attrs.update(
            {'class': 'form-control rounded-pill', 'placeholder': 'slug' , 'value':'Default'})
        self.fields['phonenum'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': '06xxxxxxxx' })
        self.fields['CIN'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'CIN'})
        self.fields['birthdate'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'birthdate'})
        self.fields['cv'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['img'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['team'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3 rounded-pill', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control rounded-pill', 'placeholder': 'Repeat Password'})

    def verf_CIN(self):
        CIN = self.cleaned_data['CIN'].lower()
        fn= UsersBase.objects.filter(CIN=CIN)
        if fn.count():
            raise forms.ValidationError("CIN already exists")
        return CIN

    def verf_phonenum(self):
        phonenum = self.cleaned_data['phonenum']
        fn= UsersBase.objects.filter(phonenum=phonenum)
        if fn.count():
            raise forms.ValidationError("phonenum already exists")
        return phonenum
        
    def verf_pswrd2(self):
        cl_dt = self.cleaned_data
        if cl_dt['password'] != cl_dt['password2']:
          raise forms.ValidationError('Passwords do not match ')
        return cl_dt['password2']

    def Verifyemail(self):
        email = self.cleaned_data['email'].lower()
        if UsersBase.objects.filter(email=email).exists():
            raise forms.ValidationError('Please use another Email, Email already exists')
        return email




class UserLoginForm(forms.Form):
    
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3 rounded-pill', 'placeholder': 'email', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control rounded-pill',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))

    class Meta():
        model = UsersBase
        fields = ("email", "password")


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not UsersBase.objects.filter(email=email).exists():
            raise forms.ValidationError("User with this email doesnot exist! Create an account instead")
        return email


