from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
  return render(request, 'bandsite_app/index.html')

def merch(request):
  return render(request, 'bandsite_app/merch.html')

def tour(request):
  return render(request, 'bandsite_app/tour.html')

def listen(request):
  return render(request, 'bandsite_app/listen.html')

#band admin access only

def admin(request):
  return render(request, 'bandsite_app/admin.html')

def login(request):
  return redirect(request, "/dashboard")

def dashboard(request):
  return render(request, 'bandsite_app/dashboard.html')