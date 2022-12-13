from urllib import response
from django.http import Http404
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest, Movies , Reservation
from .serializers import GuestSerializers, MoviesSerializers
from rest_framework.decorators import api_view 
from rest_framework import status , mixins, generics , filters , viewsets
from rest_framework.response import Response 
from rest_framework.decorators import APIView 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import   IsAuthenticated


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

#1.2 fbv movie search (get)
@api_view (['GET'])
def movies(request):
    movie = Movies.objects.filter ( pk = request.data['pk'])
    serializers = MoviesSerializers(movie, many= True)
    return Response(serializers.data)



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

#2.1class based view (get , put, delete) // for>> id=pk 
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

#3 mixins (get , post)
class Mixins_list(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializers

    def get(self , request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


#3.1 mixins (get , put , delete)
class mixins_pk(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = Guest.objects.all()
    serializer_class = GuestSerializers

    def get(self, request, pk):
        return self.retrieve(request , pk)

    def put(self, request, pk):
        return self.update(request ,pk)
    
    def delete(self, request, pk):
        return self.destroy(request , pk)


#4 generic (get , post)
class Generics_list(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializers
    
    


#4.1 generic (get , put , delete)
class Generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializers
    
#5 view_sets
class viewsets_guest(viewsets.ModelViewSet , viewsets.MethodMapper):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializers


#6 new reservation(POST)
@api_view (['POST'])
def new (request):
    movie = Movies.objects.get( title = request.data['title'] ,  room= request.data['room'])
    
    guest = Guest()
    guest.name = request.data['name'] 
    guest.mobile = request.data['mobile']
    guest.age = request.data['age']
    guest.save()

    reservation=Reservation()
    reservation.movie = movie
    reservation.guest = guest
    reservation.date = request.data['date']
    reservation.save()

    return Response( status=status.HTTP_201_CREATED)






