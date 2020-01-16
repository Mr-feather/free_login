from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from web.auth import AdminAuth, APPAuth
from web.redis_client import RedisClient


class Login(APIView):

    def get(self, request, *args, **kwargs):
        rq = request.query_params
        user_name = rq.get('user_name')

        if user_name == 'admin':
            RedisClient.set_dict(user_name, {
                'user_id': 1,
                'user_name': '超级管理员',
                'role': 'admin',
                'account': '1001',
                'list_account': '1002,1003,1004',
            })
        else:
            RedisClient.set_dict(user_name, {
                'user_id': 1,
                'user_name': '销售',
                'role': 'tmr',
                'account': user_name,
                'list_account': '1002,1003,1004',
            })

        return Response({'token': user_name}, status=status.HTTP_200_OK)


class Admin(APIView):
    authentication_classes = (AdminAuth,)

    def get(self, request, *args, **kwargs):
        print(request.user)
        return Response({'msg': 'success'}, status=status.HTTP_200_OK)


class APP(APIView):
    authentication_classes = (APPAuth,)

    def get(self, request, *args, **kwargs):
        print(request.user)
        return Response({'msg': 'success'}, status=status.HTTP_200_OK)
