from django.contrib.auth.models import User


from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    """авторизация"""
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
    
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
                  'username',)
                  
