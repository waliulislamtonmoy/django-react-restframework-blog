from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import parsers
from .models import Blog 
from .serializer import BlogSerializer
# Create your views here.

class BlogViewSet(ModelViewSet):
    queryset=Blog.objects.all().order_by("-id")
    serializer_class=BlogSerializer
    parser_classes=[parsers.FormParser,parsers.JSONParser,parsers.MultiPartParser]
    lookup_field="slug"

