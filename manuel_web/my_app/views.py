from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.
def home(request):
    return render(request, "index.html")