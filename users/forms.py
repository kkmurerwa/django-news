from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


# Forms
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('fullname', 'email', 'age', 'sex',)


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ('fullname', 'email', 'username', 'age', 'sex',)
