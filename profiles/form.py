from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea
from django.contrib.auth.models import User
from django import forms
from .models import Profile, Feddback


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # Meta inspects the current model of the class User, then ensures that 6 of the fields inside of it are there
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'second_name', 'gender', 'mobile', 'blood', 'NID', 'image')


class FeedbackFrom(forms.ModelForm):
    class Meta:
        model = Feddback
        fields = ('Email', 'Subject', 'Body')
        widgets = {
            'Body': Textarea(attrs={"rows": 5, "cols": 20}),

        }
