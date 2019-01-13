from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
  return render(request, 'bandsite_app/index.html')

def merch(request):
  return render(request, 'bandsite_app/merch.html')

def tour(request):
  return render(request, 'bandsite_app/tour.html')

def listen(request):
  return render(request, 'bandsite_app/listen.html')

def register(request):
  form = UserCreationForm()
  return render(request, 'bandsite_app/register.html', {'form': form})
