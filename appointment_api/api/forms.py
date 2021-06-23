from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import ApiUser


class ApiUserCreationForm(UserCreationForm):
    class Meta:
        model = ApiUser
        fields = ('phone', 'name', 'groups',)


class ApiUserChangeForm(UserChangeForm):
    class Meta:
        model = ApiUser
        fields = ('phone', 'name', 'groups',)