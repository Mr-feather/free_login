import rsa
import binascii

with open('public.pem', 'rb') as file:
    public_pem = rsa.PublicKey.load_pkcs1(file.read())

with open('private.pem', 'rb') as file:
    private_pem = rsa.PrivateKey.load_pkcs1(file.read())
print(public_pem)

crypt = rsa.encrypt("hello".encode('utf-8'), public_pem)


def rsa_encrypt(message):
    message = rsa.encrypt(message.encode('U8'), public_pem)
    return binascii.b2a_base64(message).decode()


def rsa_decrypt(auth_sequence):
    return rsa.decrypt(binascii.a2b_base64(auth_sequence), private_pem)


if __name__ == '__main__':
    print('输入客户端获取的序列号码：')
    abc = input()
    crypt = rsa_encrypt(abc)
    print("授权序列：")
    print(crypt)
