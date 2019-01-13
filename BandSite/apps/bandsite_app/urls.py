from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),#root route
    url(r'^merch$', views.merch), #view merch page route
    url(r'^checkout$', views.checkout), #allows you to keep track of merch amounts
    url(r'^tour$', views.tour), #view tour dates page route
    url(r'^listen$', views.listen) # view the listening page route

]