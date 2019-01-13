from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import User, Tour, Product
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
  return render(request, 'bandsite_app/index.html')

def merch(request):
  return render(request, 'bandsite_app/merch.html')

def tour(request):
  return render(request, 'bandsite_app/tour.html')

def listen(request):
  return render(request, 'bandsite_app/listen.html')

# def register(request):
#   form = UserCreationForm()
#   return render(request, 'bandsite_app/register.html', {'form': form})

def checkout(request):
  pass

def admin(request):
  return render(request, 'bandsite_app/admin.html')

def dashboard(request):

  if 'user_id' not in request.session:
    return redirect('bandsite:dashboard')

  context = {
    "managers": User.objects.all()
  }
  return render(request, 'bandsite_app/tour.html', context)

def create(request):
  errors = User.objects.validate(request.POST)
  if errors:
    for error in errors:
      messages.error(request, error)
    return redirect('bandsite:admin')
  # create and login user
  user = User.objects.create_user(request.POST)
  request.session['user_id'] = user.id
  return redirect('bandsite:dashboard')

def login(request):
  valid, result = User.objects.check_login(request.POST)
  if not valid:
    for error in result:
      messages.error(request, error)
    return redirect('bandsite:admin')

  request.session['user_id'] = result.id
  return redirect('bandsite:dashboard')

def logout(request):
  request.session.clear()
  return redirect('bandsite:index') 

def newTour(request):
  if 'user_id' not in request.session:
    return redirect('bandsite:admin')

  if request.method != 'POST':
    return redirect('bandsite:dashboard')

  errors = Tour.objects.validate(request.POST)
  if errors:
    for error in errors:
      messages.error(request, error)
    return redirect('bandsite:dashboard')

  Tour.objects.create_tour(request.POST)
  return redirect('bandsite:tour')