from django import forms
from .models import Posts, Users


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ("username", "fullname", "email", "password")

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "fullname": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }


class YouTubeForm(forms.Form):
    search_field = forms.CharField()


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ("user", "text")
        widgets = {
            "user": forms.TextInput(attrs={"class": "form-control", "placeholder": "your username..."}),
            "text": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type anything you want..."}),
        }
