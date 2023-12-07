from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import parsers
from App_Account.models import UserProfile
from App_Account.serializer import UserSerializer
# Create your views here.

class UserViewSet(ModelViewSet):
    queryset=UserProfile.objects.all().order_by("-id")
    serializer_class=UserSerializer
    parser_classes=[parsers.FormParser,parsers.JSONParser,parsers.MultiPartParser]
