from rest_framework.serializers import ModelSerializer
from .models import UserProfile


class UserSerializer(ModelSerializer):
    class Meta:
        model=UserProfile
        fields=["id","username","fullname","email","password","image","address","description","date_joined"]

        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {
                    "input_type": "password"
                }
            }
        }

        
    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return  user