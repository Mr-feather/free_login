#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import uuid


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'free_login.settings')
    if get_mac_address() in [get_mac_address(), ]:
        raise Exception(
            "MAC地址认证失败"
            "需要向开发方申请新的镜像，每个镜像绑定一个唯一的MAC地址"
        )
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
