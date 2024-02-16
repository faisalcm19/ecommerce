from django import forms
from django.contrib.auth.models import User
from ecom.models import Carts,Oders

class UserRegister (forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']

        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'first_name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'last_name'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
        }

class UserLogin(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']       

        widgets={
        
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'user_name'}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':'password'}),
            
        } 


class CartForm(forms.ModelForm):
    class Meta:
        model=Carts
        fields=['quantity']

        widgets={
        
            'quantity':forms.NumberInput(attrs={'class':'form-control'}),
            
            
        } 

class OdersForm(forms.ModelForm):
    class Meta:
        model=Oders
        fields=['address','email']

        widgets={
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            
        }