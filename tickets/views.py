from urllib import response
from django.http import Http404
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest, Movies , Reservation
from .serializers import GuestSerializers
from rest_framework.decorators import api_view 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView

#1  function based view

@api_view (['GET', 'POST'])
def fbv_list (request):
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
        

 #1.1 fbv_pk       
@api_view (['GET', 'PUT', 'DELETE'])
def fbv_pk (request , pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
     #GET
    if request.method == 'GET':
        serializer = GuestSerializers(guest)
        return Response(serializer.data)
    #PUT
    elif request.method == 'PUT':
        serializer = GuestSerializers(guest , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    #DELETE
    if request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#2 Class based view // for >> view 
class Cbv_list (APIView):
    def get(self, request):
         guest= Guest.objects.all()
         serializer = GuestSerializers(guest, many=True)
         return Response(serializer.data)

    def post(self, request):   
         serializer = GuestSerializers(guest,  data= request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
         return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

#class based view (get , put, delete) // for>> id=pk 
class Cbv_pk(APIView):
    def get_object(self, pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializers(guest)
        return Response(serializer.data)

    def put(self, request ,pk):
        guest = self.get_object(pk)
        serializer = GuestSerializers(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

    def delete (self,request ,pk):
        guest= self.get_object(pk)
        guest.delete
        return Response(status=status.HTTP_204_NO_CONTENT)
