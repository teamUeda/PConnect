from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import forms

from accounts.models import User


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'ユーザーID'
        self.fields['password'].widget.attrs['placeholder'] = 'パスワード'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class UserCreateForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_id'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['user_id'].widget.attrs['placeholder'] = 'ユーザーID'
        self.fields['password1'].widget.attrs['placeholder'] = 'パスワード'
        self.fields['password2'].widget.attrs['placeholder'] = 'パスワード(再確認)'


    class Meta:
        model = User
        fields = ("user_id", "password1", "password2",)
