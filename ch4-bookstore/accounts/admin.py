from django.contrib import admin
from .models import CostumUser
from .forms import CostumUserChangeForm, CostumUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.
CostumUser = get_user_model()

class CostumUserAdmin(UserAdmin):
    add_form = CostumUserCreationForm
    form = CostumUserChangeForm
    model = CostumUser
    list_display = [
        'email',
        'username',
        'is_superuser',
    ]

admin.site.register(CostumUser,CostumUserAdmin)