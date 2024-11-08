from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

# Form đăng ký người dùng
class UserRegistrationForm(UserCreationForm):
    dob = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY'})
    )
    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'userID', 'dob', 'gender', 'phone', 'address', 'email', 'password1', 'password2']
        labels = {
            'username': 'UserName',
            'first_name': 'Full name',
            'userID': 'CitizenID',
            'dob': 'Date of Birth',
            'gender': 'Gender',
            'phone': 'Phone number',
            'address': 'Address',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Repeat Password',
        }
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'user'
        if commit:
            user.save()
        return user

# Form đăng ký quản trị viên
class AdminRegistrationForm(UserCreationForm):
    dob = forms.DateField(
        input_formats=['%d/%m/%Y'], 
        widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY'})
    )
    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'userID', 'dob', 'gender', 'phone', 'address', 'email', 'password1', 'password2']
        labels = {
            'username': 'UserName',
            'first_name': 'Full name',
            'userID': 'AdminID',
            'dob': 'Date of Birth',
            'gender': 'Gender',
            'phone': 'Phone number',
            'address': 'Address',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Repeat Password',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'admin'
        if commit:
            user.save()
        return user

class TennisForm(forms.ModelForm):
    class Meta:
        model = Tennis
        fields = ['name', 'price', 'squared', 'limit', 'court_address', 'image', 'digital', 'brief', 'startTime', 'endTime', 'hours']  
