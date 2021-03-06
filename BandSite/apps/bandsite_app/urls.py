from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),#root route
    url(r'^merch$', views.merch, name ="merch"), #view merch page route
    url(r'^shopping_cart$', views.shopping_cart, name="cart"),
    url(r'^empty_cart$', views.empty_cart, name="emptyCart"),
    url(r'^checkout$', views.checkout, name ="checkout"), #allows you to keep track of merch amounts
    url(r'^tour$', views.tour, name ="tour"), #view tour dates page route
    url(r'^listen$', views.listen, name ="listen"), # view the listening page route

    #admin access only
    # url(r'^addtourdate$', views.addtourdate),
    url(r'^admin$', views.admin, name ="admin"), #loads the admin page
    url(r'^login$', views.login, name ="login"), #logs in the user
    url(r'^create/$', views.create, name ="create"), #creates a new user 
    url(r'^dashboard/$', views.dashboard, name ="dashboard"), #loads dashboard user page
    url(r'^newTour/$', views.newTour, name ="newTour"), #adds a new tour 
    url(r'^logout$', views.logout, name ="logout"), #logs out the user
    url(r'^edit/(?P<tour_id>\d+)$', views.edit), #loads the edit tour page
    url(r'^delete/(?P<tour_id>\d+)$', views.delete)

]