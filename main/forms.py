from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class AddInvestorForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
       super(AddInvestorForm, self).__init__(*args, **kwargs)
       del self.fields['password1']
       del self.fields['password2']

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

