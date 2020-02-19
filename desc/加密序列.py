import rsa
import binascii

with open('public.pem', 'rb') as file:
    public_pem = rsa.PublicKey.load_pkcs1(file.read())


def rsa_encrypt(message):
    message = rsa.encrypt(message.encode('U8'), public_pem)
    return binascii.b2a_base64(message).decode()


if __name__ == '__main__':
    print('输入客户端获取的序列号码：')
    abc = input()
    crypt = rsa_encrypt(abc)
    print("授权序列：")
    print(crypt)
