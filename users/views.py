# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
# from rest_framework import generics, permissions
# from .models import User
# from .serializer import UserSerializer, MyTokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# def helloWorld(request):
#     return HttpResponse("Hello World")

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
#     permission_classes = (AllowAny, )


# class LogoutView(APIView):
    

#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(token=refresh_token)
#             token.blacklist()
#             return Response(status=205)
#         except Exception as e:
#             return Response(status=400, data={"detail": str(e)})

# class TokenRefreshView(TokenRefreshView):
#     pass



from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenBlacklistSerializer
from .models import User
from .serializer import UserSerializer, MyTokenObtainPairSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def helloWorld(request):
    return HttpResponse("Hello World")

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TokenBlacklistSerializer

    def post(self, request):
            try:
                refresh_token = request.data["refresh"]
                #refresh_token = request.META.get('HTTP_AUTHORIZATION', '').split()[1]
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({'message':'User logout successfully'},status=status.HTTP_205_RESET_CONTENT)
            except (ObjectDoesNotExist, TokenError) as err:
                return Response({'message':str(err)},status=status.HTTP_400_BAD_REQUEST)
      
