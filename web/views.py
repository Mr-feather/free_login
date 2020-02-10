from tracemalloc import BaseFilter

from django.shortcuts import render

# Create your views here.
from rest_framework import status, mixins, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from web.auth import AdminAuth, APPAuth
from web.models import SS
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

    def initialize_request(self, request, *args, **kwargs):
        """
        Returns the initial request object.
        """
        parser_context = self.get_parser_context(request)

        return Request(
            request,
            parsers=self.get_parsers(),
            authenticators=[APPAuth()] if request.method.lower() == "get" else [AdminAuth()],
            negotiator=self.get_content_negotiator(),
            parser_context=parser_context
        )

    def get(self, request, *args, **kwargs):
        print(request.user)
        return Response({'msg': 'success'}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return Response({'msg': 'success'}, status=status.HTTP_200_OK)


class APP(APIView):
    authentication_classes = (APPAuth,)

    def get(self, request, *args, **kwargs):
        print(request.user)
        return Response({'msg': 'success'}, status=status.HTTP_200_OK)


class BaseViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    后台管理使用
    对于get方法取数的 ，后台和坐席端都要允许
    """
    permission_classes = []

    def initialize_request(self, request, *args, **kwargs):
        """
        Returns the initial request object.
        """
        self.authentication_classes = [APPAuth] if request.method.lower() == "get" else [AdminAuth]
        return super().initialize_request(request, args, kwargs)


class DissentViewSet(BaseViewSet):
    queryset = SS.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return Response({'data': '123'})
