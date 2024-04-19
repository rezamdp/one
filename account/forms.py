#==================================================> Imports <==================================================
# ----> genrel imports <----
from django import forms
from django.contrib.auth.forms import (
    UserCreationForm ,UserChangeForm)

# ----> extrenal imports <----
from .models import *




#===============================================> EditUser Form <===============================================

class EditUserForm (UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'phone_number',
                  'is_verified',
                  'is_staff',
                  'is_superuser',
                  'images_user',
                  ]


#================================================> CreateUser Form <=================================================

class CreateUserForm (UserCreationForm ):
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'phone_number',
                  'images_user',


                  ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'تلفن همراه'}),


        }

