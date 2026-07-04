from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post,Comment



class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Email'
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Choose Username'
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Create Password'
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Confirm Password'
            }
        )
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


# ==========================
# EDIT PROFILE FORM
# ==========================

class ProfileUpdateForm(forms.ModelForm):

    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'rows':4,
                'placeholder':'Tell us about yourself...'
            }
        )
    )

    profile_pic = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    class Meta:
        model = Profile
        fields = [
            'bio',
            'profile_pic'
        ]



class PostForm(forms.ModelForm):

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': "What's on your mind?"
            }
        )
    )

    class Meta:
        model = Post
        fields = [
            'content',
            'image'
        ]

class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment

        fields = ["text"]

        widgets = {
            "text": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write a comment..."
                }
            )
        }