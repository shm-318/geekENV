from django import forms
from .models import *

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