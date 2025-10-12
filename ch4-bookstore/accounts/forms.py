from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CostumUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'username',
        ]

class CostumUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'username',
            
        ]