from django.contrib.auth import authenticate

from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import *


@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    """
    Авторизация пользователя
    необходимо отправить json в body вида:

    { 
    "username": "username",
    "password": "123456"
    }
    """

    login_serializer = UserLoginSerializer(data=request.data)

    if not login_serializer.is_valid():
        return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(
        username=login_serializer.data['username'],
        password=login_serializer.data['password']
    )

    if not user:
        return Response({'detail': 'Неправильные данные для входа в аккаунт'},
                        status=status.HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)

    user_serialized = UserSerializer(user)

    return Response({
        'user': user_serialized.data,
        'token': token.key
    }, status=status.HTTP_200_OK)
