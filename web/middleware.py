from django.shortcuts import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
import uuid


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


class MacMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if get_mac_address() in [get_mac_address(), ]:
            pass
        else:
            raise Exception(
                "MAC地址认证失败"
                "需要向开发方申请新的镜像，每个镜像绑定一个唯一的MAC地址"
            )
