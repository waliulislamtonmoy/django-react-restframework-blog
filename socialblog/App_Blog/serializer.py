from rest_framework.serializers import ModelSerializer 
from .models import Blog 

from App_Account.models import UserProfile

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model=UserProfile
        fields=["id","fullname","email","address","image"]
        

class BlogSerializer(ModelSerializer):
    class Meta:
        model=Blog
        fields="__all__"
        read_only_fields=["author"]
        lookup_field="slug"
        depth=1
    def to_representation(self, instance):
        data=super().to_representation(instance)
        data['author']=UserProfileSerializer(instance.author).data 
        return data