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
  return render(request, 'bandsite_app/merch.html', merch_count=merch_count)


def tour(request):
  return render(request, 'bandsite_app/tour.html')

def listen(request):
  return render(request, 'bandsite_app/listen.html')