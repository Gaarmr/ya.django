from .forms import CreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.
class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login") #  где login — это параметр "name" в path()
    template_name = "signup.html"
