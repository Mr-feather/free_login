import binascii

from desc.py_des import des, ECB, PAD_PKCS5

iv = secret_key = 'K$KeZY$K'
k = des(secret_key, ECB, iv, pad=None, padmode=PAD_PKCS5)


class DesUtils(object):
    @staticmethod
    def encrypt(content):
        """
        DES 加密
        :param content: 原始字符串
        :return: 加密后字符串，16进制
        """
        if isinstance(content, int):
            content = str(content)
        en = k.encrypt(content, padmode=PAD_PKCS5)
        return binascii.b2a_hex(en).decode('utf-8').upper()

    @staticmethod
    def un_encrypt(content: str):
        """
        DES 解密
        :param content: 加密后的字符串，16进制
        :return:  解密后的cid
        """
        de = k.decrypt(binascii.a2b_hex(content), padmode=PAD_PKCS5)
        return de.decode('utf-8')


if __name__ == '__main__':
    str_en = DesUtils.encrypt('6c:40:08:9f:5b:54')
    print(str_en)
    str_de = DesUtils.un_encrypt('0053761EB43CE14D642B162C1F35AB7E1C25C4ABAEDC883D')
    print(str_de)

    print(DesUtils.encrypt(185196))
    print(DesUtils.encrypt(48336))
