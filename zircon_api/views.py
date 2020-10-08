from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from . import models
from . import serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class SignupViewSet(viewsets.ViewSet):
    serializer_class = serializers.SignupSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            signup_user = models.InstaGramUser.objects.create_user(
                username=serializer.data['username'],
                email=serializer.data['email'],
                password=serializer.data['password'],
                full_name=serializer.data['full_name'],
            )
            print(signup_user)
            if signup_user:
                status_code = status.HTTP_201_CREATED
                return Response({'success': 'True', 'status code': status_code, 'message': 'User registered  successfully', })
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(viewsets.ViewSet):
    serializer_class = serializers.LoginSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token': serializer.data['token'],
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

        # serializer = self.serializer_class(data=request.data)
        # if serializer.is_valid():
        #     signup_user = models.InstaGramUser.objects.create_user(
        #         username=serializer.data['username'],
        #         email=serializer.data['email'],
        #         password=serializer.data['password'],
        #         full_name=serializer.data['full_name'],
        #     )
        #     print(signup_user)
        #     if signup_user:
        #         return Response({'status': 'signup successful'})
        #     else:
        #         return Response(serializer.errors,
        #                         status=status.HTTP_400_BAD_REQUEST)
