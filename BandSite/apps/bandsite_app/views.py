from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import User, Tour, Product
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
  return render(request, 'bandsite_app/index.html')

def merch(request):
  request.session['cart'] = 0
  return render(request, 'bandsite_app/merch.html')

def tour(request):
  context = {
    # 'tours': Tour.objects.filter(manager=request.session['user_id']),
    # 'user_info': User.objects.get(id=request.session['user_id']),
    'tours': Tour.objects.all(),
    'managers': User.objects.all()
  }
  print(Tour.objects.all())
  return render(request, 'bandsite_app/tour.html', context)

def listen(request):
  return render(request, 'bandsite_app/listen.html')

# def register(request):
#   form = UserCreationForm()
#   return render(request, 'bandsite_app/register.html', {'form': form})
def shopping_cart(request):
  request.session['cart'] = 0
  if request.method == 'POST':
    merch_amount = request.POST['merch']
    print(merch_amount)
    request.session['cart'] = request.session['cart'] + int(merch_amount)
    print(request.POST)
    return render(request, 'bandsite_app/merch.html')
  
  #for key, value in request.session.item():
    #print('{} => {}'.format('key, value'))
  #item = request.POST['merch']
  #request.session['cart'] = int(request.session['cart']) + int(item)
def empty_cart(request):
  del request.session['cart']
  return render(request, 'bandsite_app/merch.html')

def checkout(request):
  # Set your secret key: remember to change this to your live secret key in production
  # See your keys here: https://dashboard.stripe.com/account/apikeys
  stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
  # Token is created using Checkout or Elements!
  # Get the payment token ID submitted by the form:
  token = request.form['stripeToken'] # Using Flask
  charge = stripe.Charge.create(
      amount='request.session.cart',
      currency='usd',
      description='Example charge',
      source=token,
      metadata={'order_id': 6735},
  )
  return render(request, 'bandsite_app/merch.html', merch_count=merch_count)

def admin(request):
  return render(request, 'bandsite_app/admin.html')

def dashboard(request):

  if 'user_id' not in request.session:
    return redirect('bandsite:admin')
  
  context = {
    "managers": User.objects.all()
  }
  return render(request, 'bandsite_app/dashboard.html', context)

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

def edit(request, tour_id):
  #code protecting route from unlogged users editing tour. 
  if 'user_id' not in request.session:
    return redirect('bandsite:admin')
  #code protecting route from non-tourmanagers editing tour. 
  if 'user_id' != request.session["user_id"]:
    request.session.clear()
    return redirect('bandsite:admin')
  tour = Tour.objects.get(id=tour_id)
  context = {
    "tour" : Tour.objects.get(id=tour_id),
    "managers": User.objects.all()
  }
  return render(request, "bandsite_app/edittour.html", context)

def delete(request, tour_id):
  #code protecting route from unlogged users editing tour. 
  if 'user_id' not in request.session:
    return redirect('bandsite:admin')
  #code protecting route from non-tourmanagers editing tour. 
  if 'user_id' != request.session["user_id"]:
    request.session.clear()
    return redirect('bandsite:admin')
  tour = Tour.objects.get(id=tour_id)
  Tour.objects.delete_tour(tour_id)
  return redirect('bandsite:tour')
