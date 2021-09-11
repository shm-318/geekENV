from django import forms
from .models import *
from django.contrib.auth import get_user_model
#from blog.models import User

User = get_user_model()

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
        fields = ('full_name', 'email', 'username','phone_number','gender' ,'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('full_name', 'email', 'username',)


#user edit form
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'picture_url',
            'full_name',
            'username',
            'email',
            'status',
            'college',
            'country',
            'website',
            'phone_number',
            'gender',
            
            )
        labels = {
            
            'phone_number': 'Phone'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control form-control-sm'})