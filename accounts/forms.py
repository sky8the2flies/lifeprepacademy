from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'promo_code', 'password1', 'password2')


class StudentRegister(UserCreationForm):
    class Meta:
        model = get_user_model()
        labels = {
            'username': 'Student Username',
        }
        fields = ('username', 'password1', 'password2')
