from django import forms
from django.forms import TextInput, EmailInput, PasswordInput 
from .models import UserDetails,ShareDetails

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = '__all__'
        labels = {'first_name':'First Name :', 'last_name':'Last Name :', 'user_name':'User Name :', 'email':'Email ID :', 'password':'Password :'}
        widgets = {
            "first_name": TextInput(attrs={"class": 'form-control'}),
            "last_name": TextInput(attrs={"class": 'form-control'}),
            "user_name": TextInput(attrs={"class": 'form-control'}),
            "email": EmailInput(attrs={"class": 'form-control'}),
            "password": PasswordInput(attrs={"class": 'form-control'}),
            }

class UserloginForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['email','password']
        labels = {'email':'Email ID :', 'password':'Password :'}
        widgets = {
            "email": EmailInput(attrs={"class": 'form-control'}),
            "password": PasswordInput(attrs={"class": 'form-control'}),
            }
        
class AddSharesForm(forms.ModelForm):
    class Meta:
        model = ShareDetails
        fields = ['comp_name','price','quantity','userid']
        labels = {'comp_name':'Company Name :', 'price':'Price :', 'quantity':'Quantity :'}
        widgets = {
            # "dop": TextInput(attrs={"class": 'form-control'}),
            "comp_name": TextInput(attrs={"class": 'form-control'}),
            "price": TextInput(attrs={"class": 'form-control'}),
            "quantity": TextInput(attrs={"class": 'form-control'}),
            "userid": forms.Select( attrs={'class': 'form-control'}),
            # "userid": forms.CharField(disabled = True)
            # "userid": forms.Select(widgets = forms.HiddenInput(), required = False,attrs={'class': 'form-control'})
            }