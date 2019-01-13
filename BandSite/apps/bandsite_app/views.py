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

def register(request):
  form = UserCreationForm()
  return render(request, 'bandsite_app/register.html', {'form': form})

def checkout(request):
  pass

def admin(request):
  return render(request, 'bandsite_app/admin.html')

def login(request):
  users = User.objects.filter(email=request.POST["email"])#retrieve record in database to see if email exists
  if len(users) > 0: #if I found a user
    user = users[0]
    if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):   #checking to make sure the password is correct
      request.session['id'] = user.id 
      return redirect('/dashboard')
  messages.error(request, 'invalid credentials')#if either of the above if's fail
  return redirect('/admin')

def dashboard(request):
  return render(request, 'bandsite_app/dashboard.html')

def created(request):
  pass

