from django.shortcuts import render
from rest_framework.views import APIView
from .serialisers import *
from .models import profile
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated



class UserView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthenticated]
    def get(self, request):
        try:
            queryset = profile.objects.all()
            serializer = profile_serialiser(queryset,many=True)
            return Response(serializer.data)
        except:
            return Response({'message':'Ther no profile data is availabele'})

    def post(self, request):
        serializer=profile_serialiser(request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'message':'data is created successfully'},serializer.data)
        return Response(serializer.errors)

class Detail_Views(APIView):

    def get(self, request,pk=None,*args,**kwargs):
        try:
            queryset = profile.objects.get(pk=pk)
            serializer = profile_serialiser(queryset)
            return Response(serializer.data)
        except profile.DoesNotExist:
            return Response({'message':'Ther no profile data is availabele'})

    def put(self,request,pk=None,*args,**kwargs):
        queryset=get_object_or_404(profile,pk=pk)
        serializer=profile_serialiser(instance=profile,initial=queryset,data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'message':'data is updated successfully'},serializer.data)
        return Response(serializer.errors)

    def delete(self,request,pk=None,*args,**kwargs):
        try:
            obj = profile.objects.get(pk=pk)
            status, object_deleted = obj.delete()
            print(status)
            if status == 1:
                return Response(
                    {'msg': 'The data with the id {} is succeccfully deleted'.format(id)})

            return Response(
                {'msg': 'Sorry! we are unable to process your data please try again'})

        except profile.DoesNotExist:
            error_msg = {'msg': 'This data is not found in our database so no such student with this id::'}
            return Response(error_msg, status=400)

