from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Tour, Product

# Create your views here.
def index(request):
  return render(request, 'bandsite_app/index.html')

def merch(request):
  return render(request, 'bandsite_app/merch.html')

def checkout(request):
  print(request.form)
  merch_count = int(request.POST['record']) + int(request.POST['tshirt']) + int(request.POST['hoodie'])
  print(merch_count)
  return render(request, 'bandsite_app/merch.html', merch_count=merch_count)


def tour(request):
  return render(request, 'bandsite_app/tour.html')

def listen(request):
  return render(request, 'bandsite_app/listen.html')

#band admin access only

def admin(request):
  return render(request, 'bandsite_app/admin.html')

def login(request):
  return redirect(request, '/dashboard')

def dashboard(request):
  return render(request, 'bandsite_app/dashboard.html')

def created(request):
  # errors = User.objects.validate(request.POST)
  # if errors:
  #   for error in errors:
  #     messages.error(request, error)
  #   return redirect("/admin")
  # #create and login user
  # user = User.objects.create_user(request.POST)
  # request.session['first_name'] = request.POST['first_name']
  # messages.success(request, "Successfully registered!")
  # # return render(request, 'bandsite_app/dashboard.html') #this works
  return redirect(request, '/dashboard') #this does not work
  