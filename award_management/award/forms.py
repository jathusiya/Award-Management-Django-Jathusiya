# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from award_management.award.models import User

# class CustomUserForm(UserCreationForm):
#     username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
#     firstname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}))
#     lastname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}))
#     email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
#     password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password1'}))
#     password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm password2'}))
#     class meta:
#         model=User
#         fields=['username','email','firstname','lastname','password1','password2']

# class LoginForm(AuthenticationForm):
#     # You can customize this form as needed
#     pass
