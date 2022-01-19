
from django.shortcuts import render
from .models import OrderItem
from rest_framework.decorators import api_view
from .serializers import OrderItemsSerializer
from rest_framework.response import Response

from django.contrib.auth.models import User 

from django.contrib.auth import authenticate, login, logout
# Create your views here.

@api_view(['POST'])
def orderitem_view(request):
    serializer = OrderItemsSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

def chef_view(request):
    return render(request,'testapp/chef.html')









