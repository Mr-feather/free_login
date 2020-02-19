import rsa  # line:1
import binascii  # line:2
import os  # line:3
import uuid  # line:4
from utils import des, ECB, PAD_PKCS5  # line:6

AUTH = "AhIx9puB4WALzc0LEc6MS5oI8Gwr4zYSY0Mf1WmH3eNZmCg//OOeyDxSJqwZmBO+XOHB+1pAjrzXer0mtcB2Qs8JEcV1Xj9UG7f8gxuW93Q8/Tl5DTpgnewSVmWF+fX22DFuhVEeVfyvl9nTdf/6Xvqq9Y9N4GacJRDiWdBHoO/zmEi97292YYl6Fi/GyzoM9ElA+kUbYKItxJPJ4ew="  # line:8
iv = secret_key = 'K$KeZY$K'  # line:9
k = des(secret_key, ECB, iv, pad=None, padmode=PAD_PKCS5)  # line:10


def get_mac_address():  # line:13
    OO000000O0O0OO000 = uuid.UUID(int=uuid.getnode()).hex[-12:]  # line:14
    return ":".join([OO000000O0O0OO000[O00OOO000O0OOOOO0:O00OOO000O0OOOOO0 + 2] for O00OOO000O0OOOOO0 in
                     range(0, 11, 2)])  # line:15


class DesUtils(object):  # line:18
    @staticmethod  # line:19
    def encrypt(O0OO0O00OOOO0O00O):  # line:20
        ""  # line:25
        if isinstance(O0OO0O00OOOO0O00O, int):  # line:26
            O0OO0O00OOOO0O00O = str(O0OO0O00OOOO0O00O)  # line:27
        O0OO00OOO00000O00 = k.encrypt(O0OO0O00OOOO0O00O, padmode=PAD_PKCS5)  # line:28
        return binascii.b2a_hex(O0OO00OOO00000O00).decode('utf-8').upper()  # line:29


with open('private.pem', 'rb')as file:  # line:32
    private_pem = rsa.PrivateKey.load_pkcs1(file.read())  # line:33


def rsa_decrypt(O000OOOOO0O0O0000):  # line:36
    return rsa.decrypt(binascii.a2b_base64(O000OOOOO0O0O0000), private_pem).decode()  # line:37


def auth_auth_sequence(O0OO00OOO0O0O0OOO):  # line:40
    try:  # line:41
        OOO00000O000OO0O0 = DesUtils.encrypt(get_mac_address())  # line:42
        if OOO00000O000OO0O0 == rsa_decrypt(O0OO00OOO0O0O0OOO):  # line:43
            return True  # line:44
        return False  # line:45
    except Exception as OO00O0OO000O0O00O:  # line:46
        import traceback  # line:47
        print(OO00O0OO000O0O00O, traceback.format_exc())  # line:48
        return False  # line:49


if __name__ == '__main__':  # line:52
    auth_sequence = os.getenv('AUTH_SEQUENCE', AUTH)  # line:53
    print(auth_auth_sequence(auth_sequence))  # line:54
