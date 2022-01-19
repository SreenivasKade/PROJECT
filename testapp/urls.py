from django.urls import path
from testapp import views

urlpatterns = [
    path('orderitem/',views.orderitem_view),
    path('chef/',views.chef_view),
   
  
]