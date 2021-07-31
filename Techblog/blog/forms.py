from django import forms
from .models import *
from django.contrib.auth import get_user_model
from blog.models import User

class ContactForm(forms.ModelForm):
    
    class Meta():
        model=Contact
        fields= '__all__'

        widgets={
            'Name': forms.TextInput(attrs={'placeholder':'Enter your name'}),
            'Email': forms.EmailInput(attrs={'placeholder':'Enter your email'}),
            'Message':forms.TextInput(attrs={'placeholder':'Enter you message to be sent'}),
            'ContactNo':forms.NumberInput(attrs={'placeholder':'Enter your contact no'})
        }



from django.contrib.auth.forms import UserCreationForm, UserChangeForm
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('full_name', 'email', 'username', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('full_name', 'email', 'username',)