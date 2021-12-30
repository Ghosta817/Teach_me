alf = [str(i) for i in input()]
dq_alf = [str(i) for i in input()]
text_to_encrypt = [str(i) for i in input()]
text_to_decrypt = [str(i) for i in input()]

crypt_dict, encrypt_dict = dict(), dict()
for i in range(len(alf)):
    crypt_dict[alf[i]] = dq_alf[i]
for i in range(len(dq_alf)):
    encrypt_dict[dq_alf[i]] = alf[i]

for let in text_to_encrypt:
    print(crypt_dict[let], end='')
print()
for crypt in text_to_decrypt:
    print(encrypt_dict[crypt], end='')
