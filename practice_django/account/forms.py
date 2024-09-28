from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Имя пользователя'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Подтверждение пароля'

    def clean_username(self):
        username = self.cleaned_data.get('username').strip()
        if len(username) < 3:
            raise ValidationError(
                message=f"username length < 3",
                code="username length < 3"
            )
        if ' ' in username:
            raise ValidationError(
                message="There should be no spaces in the password",
                code="invalid password"
            )
        return username


class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Имя пользователя'
        self.fields['password'].label = 'Пароль'

    def clean_username(self):
        username = self.cleaned_data.get('username').strip()
        if len(username) < 3:
            raise ValidationError(
                message=f"username length < 3",
                code="username length < 3"
            )
        if ' ' in username:
            raise ValidationError(
                message="There should be no spaces in the password",
                code="invalid password"
            )
        return username
