from django import forms
from .models import User

class StuRegis(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        widgets = {
            'name' : forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Your Name'
            }),
           'email' : forms.EmailInput(attrs={
               'class':'form-control',
               'placeholder':'Enter Your Password'
           }),
           'password' : forms.PasswordInput(render_value=True,attrs={
               'class':'form-control',
               'placeholder':'Enter Your Password'
           })
        }
        labels = {
            'name':'Name',
            'email':"Email",
            "password":"Password",
        }

        error_messages = {
            'name': {'required':'Name Must Be Required'},
            'email': {'required':'Email Must Be Required'},
            'password': {'required':'Password Must Be Required'},

        }