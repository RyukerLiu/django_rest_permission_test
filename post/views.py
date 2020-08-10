from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
