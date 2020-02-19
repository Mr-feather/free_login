# import rsa
#
# (pubkey, privkey) = rsa.newkeys(1260)
#
# with open('public.pem', mode='wb') as public_file:
#     public_file.write(pubkey.save_pkcs1())
#
# print('公钥生成。。。')
# with open('private.pem', mode='wb') as private_file:
#     private_file.write(privkey.save_pkcs1())
#
# print('私钥生成。。。')


import requests

print(requests.get('http://xxxxx'))