from django import forms
from .models import post, author, category
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateForm(forms.ModelForm):
    class Meta:
        model = post
        fields = [
            'post_title',
            'slug',
            'post_body',
            'post_image',
            'post_category',
        ]

class registerUser(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]

class createAuthor(forms.ModelForm):
    class Meta:
        model = author
        fields =[
            'auth_image',
            'auth_details',
        ]

class categoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = [
            'name'
        ]
