from django import forms
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2',)

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        exclude = [ 'id', 'password', 'date_joined' ]
        widgets = {
            'first_name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'last_name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'email': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'phone_number': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'username': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'avatar_img': widgets.TextInput(attrs={ 'class': 'form-control' }),
        }