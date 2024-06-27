from django.shortcuts import render
from rest_framework import generics
from .models import Articles
from .serializers import ArticlesSerializer

class ArticlesListCreate(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer

class ArticlesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
