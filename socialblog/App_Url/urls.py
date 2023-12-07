
from django.urls import path

from rest_framework import routers
from App_Blog.views import BlogViewSet
from App_Account.views import UserViewSet
# Create your views here.


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'blogs', BlogViewSet)

urlpatterns =[

]+ router.urls