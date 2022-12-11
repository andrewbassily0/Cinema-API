from urllib import response
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest, Movies , Reservation
from .serializers import GuestSerializers
from rest_framework.decorators import api_view 
from rest_framework import status
from rest_framework.response import Response


#1  function based view
@api_view (['GET', 'POST'])
def fbv (request):
    #GET
    if request.method == 'GET':
        guest = Guest.objects.all()
        serializer = GuestSerializers(guest , many=True)
        return Response(serializer.data)
    #POST
    elif request.method == 'POST':
        serializer = GuestSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
