from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from .models import Registration 
from .serializers import RegistrationSerializer

# Create your views here.

class RegistrationList(APIView):
    
    def get (self , request):
        registration=Registration.objects.all()
        serializer=RegistrationSerializer(registration , many=True)
        return Response (serializer.data)
    
    
    def post (self,request):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RegistrationDetail(APIView):
    
    def get (self,request,pk):
        try :
            registration=Registration.objects.get(pk=pk)
        except Registration.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer=RegistrationSerializer(registration)
        return Response(serializer.data) 
    
    def put (self,request,pk):
        try :
            registration =Registration.objects.get(pk=pk)
        except Registration.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=RegistrationSerializer(registration,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors)
    
    def delete (seelf,request,pk):
        try :
            registration= Registration.objects.get(pk=pk) 
        except Registration.DoesNotExist:
            return Response (status=status.HTTP_404_NOT_FOUND)
        
        registration.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
    
    
        