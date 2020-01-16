from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from web.redis_client import RedisClient
from django.utils.translation import ugettext_lazy as _


class APPAuth(BaseAuthentication):
    def authenticate(self, request):
        """
            Returns a `User` if a correct username and password have been supplied
            using HTTP Basic authentication.  Otherwise returns `None`.
                """
        token = request.headers.get('TOKEN', '')

        if not token:
            msg = 'Invalid header. No token provided.'
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = RedisClient.get_dict(token)
            if not user:
                raise exceptions.AuthenticationFailed(_('Invalid token.'))
            return user, None
        except (TypeError, UnicodeDecodeError):
            msg = 'Invalid header. please contract administrator'
            raise exceptions.AuthenticationFailed(msg)

    def authenticate_header(self, request):
        return 'Token'


class AdminAuth(APPAuth):
    def authenticate(self, request):
        """
            Returns a `User` if a correct username and password have been supplied
            using HTTP Basic authentication.  Otherwise returns `None`.
                """
        user, _ = super().authenticate(request)

        if user.get('role') == 'admin':
            return user, None
        else:
            raise exceptions.AuthenticationFailed('Invalid token.')
