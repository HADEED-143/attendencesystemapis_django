from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . models import Userrecord, UserMark, ViewMark
from . serializers import UserRecSerializer, UserMarksSerializer, marksviewSerializer


class Userrec(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            ur = Userrecord.objects.get(id=id)
            serializer = UserRecSerializer(ur)
            return Response(serializer.data)
        ur = Userrecord.objects.all()
        serializer = UserRecSerializer(ur, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = UserRecSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created'}, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        ur = Userrecord.objects.get(pk=id)
        serializer = UserRecSerializer(rs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete update'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        ur = Userrecord.objects.get(pk=id)
        serializers = UserRecSerializer(ur, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'updated data'})
        return Response(serializers.errors)
    def delete(self, request, pk, format=None):
        id = pk
        ur = Userrecord.objects.get(pk=id)
        ur.delete()
        return Response({'msg':'Data deleted'})




class Usermark(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            um = UserMark.objects.get(id=id)
            serializer = UserMarksSerializer(um)
            return Response(serializer.data)
        um = UserMark.objects.all()
        serializer = UserRecSerializer(um, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = UserRecSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created'}, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        um = UserMark.objects.get(pk=id)
        serializer = UserRecSerializer(um, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete update'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        um = UserMark.objects.get(pk=id)
        serializers = UserRecSerializer(um, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'updated data'})
        return Response(serializers.errors)
    def delete(self, request, pk, format=None):
        id = pk
        um = UserMark.objects.get(pk=id)
        um.delete()
        return Response({'msg':'Data deleted'})



class markview(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            rs = ViewMark.objects.get(id=id)
            serializer = marksviewSerializer(rs)
            return Response(serializer.data)
        rs = ViewMark.objects.all()
        serializer = marksviewSerializer(rs, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = marksviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created'}, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        rs = markview.objects.get(pk=id)
        serializer = marksviewSerializer(rs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete update'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        rs = markview.objects.get(pk=id)
        serializers = marksviewSerializer(rs, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'updated data'})
        return Response(serializers.errors)
    def delete(self, request, pk, format=None):
        id = pk
        rs = markview.objects.get(pk=id)
        rs.delete()
        return Response({'msg':'Data deleted'})