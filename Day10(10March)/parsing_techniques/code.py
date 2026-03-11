## dumps(): Encryption
## loads(): Decryption

'''
1. JSON
2. pickle
'''

# import json
# file=open('temp.txt','a+')
# data={
#     'fullname':'pqr',
#     'userid':12345456788,
#     'password':'******'
# }
# print(f'Original Data:{data}')
# print((f'Type of org Data:{type(data)}'))
# enc_data=json.dumps(data)
# print(f'Encrypted Data:{enc_data}')
# print(f'Type of Encrypted data:{type(enc_data)}')
# dec_data=json.loads(enc_data)
# print(f'Encrypted Data:{dec_data}')
# print(f'Type of Encrypted data:{type(dec_data)}')
# enc_data=file.read()
# print(type(enc_data))
# # ori_data=json.loads(enc_data)
# # print(ori_data,type(ori_data))
# file.close()


import pickle
file=open('temp.txt','a+')
data={
    'fullname':'pqr',
    'userid':12345456788,
    'password':'******'
}
print(f'Original Data:{data}')
print((f'Type of org Data:{type(data)}'))
enc_data=pickle.dumps(data)
print(f'Encrypted Data:{enc_data}')
print(f'Type of Encrypted data:{type(enc_data)}')
dec_data=pickle.loads(enc_data)
print(f'Encrypted Data:{dec_data}')
print(f'Type of Encrypted data:{type(dec_data)}')
enc_data=file.read()
print(type(enc_data))
# ori_data=json.loads(enc_data)
# print(ori_data,type(ori_data))