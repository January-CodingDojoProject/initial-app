from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),#root route
    url(r'^merch$', views.merch), #view merch page route
    url(r'^tour$', views.tour), #view tour dates page route
    url(r'^listen$', views.listen), # view the listening page route

    #admin access only
    # url(r'^addtourdate$', views.addtourdate),
    url(r'^admin$', views.admin), #loads the admin page
    url(r'^login$', views.login), #logs in the user
    url(r'^dashboard$', views.dashboard) #loads the dashboard page
]