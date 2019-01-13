from django.shortcuts import render, redirect

# Create your views here.
def index(request):
  return render(request, 'bandsite_app/index.html')

def merch(request):
  return render(request, 'bandsite_app/merch.html')

def checkout(request):
  print(request.form)
  merch_count = int(request.POST['record']) + int(request.POST['tshirt']) + int(request.POST['hoodie'])
  print(merch_count)
  # Set your secret key: remember to change this to your live secret key in production
  # See your keys here: https://dashboard.stripe.com/account/apikeys
  stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
  # Token is created using Checkout or Elements!
  # Get the payment token ID submitted by the form:
  token = request.form['stripeToken'] # Using Flask
  charge = stripe.Charge.create(
      amount=999,
      currency='usd',
      description='Example charge',
      source=token,
      metadata={'order_id': 6735},
  )
  return render(request, 'bandsite_app/merch.html', merch_count=merch_count)


def tour(request):
  return render(request, 'bandsite_app/tour.html')

def listen(request):
  return render(request, 'bandsite_app/listen.html')