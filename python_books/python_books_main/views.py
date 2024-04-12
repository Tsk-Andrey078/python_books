from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Book
from .models import UserProfile
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import BooksSerializer, BooksDynamicSerializer, UserProfileSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    lookup_field = 'id_b'

    
class BooksView(APIView):

    def get(self, request, format=None):
        temp_columns = UserProfile.objects.filter(is_visible=True).values_list('column_name')
        
        columns = []
        for column in temp_columns:
            columns.append(column[0])        
        books = Book.objects.values(*columns)
        print(list(books))
        books = BooksDynamicSerializer(fields=columns, data=list(books), many=True)
        print(books)
        books.is_valid(raise_exception=True)
        instance = books.data
        return Response([columns, instance])
    
class UserSettings(APIView):
    
    def get(self, request, format=None):
        data = UserProfile.objects.all()
        serializer = UserProfileSerializer(data, many=True)
        return Response(serializer.data)
    
    def put(self, request, format=None):
        print(request.data['is_visible'])
        if request.data['is_visible'] == True:
            UserProfile.objects.filter(column_name=request.data['column_name']).update(is_visible=True)
        else:
            UserProfile.objects.filter(column_name=request.data['column_name']).update(is_visible=False)
        return Response([])