from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CostumUserCreationForm
from django.views.generic import CreateView


# Create your views here.
class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CostumUserCreationForm
    success_url = reverse_lazy('login')

