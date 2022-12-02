from django.contrib.auth.models import User

from django import forms


class userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']
