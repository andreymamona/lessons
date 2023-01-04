# Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую
# нужно зашифровать, и ключ шифрования, которая возвращает строку,
# зашифрованную путем применения функции XOR (^) над символами строки с ключом.
# Написать также функцию xor_uncipher, которая по зашифрованной строке
# и ключу восстанавливает исходную строку.

def equal_length(phrase, key):
    while len(key) < len(phrase):
        key += key
    return key

# более правильное решение
# def get_key_symbol(key, index):
#     """
#     Если длина нашего ключа меньше начальной строки
#     мы получаем следующий символ с самого начала в цикле
#     """
#     if index > len(key) - 1:
#         return key[index % len(key)]
#     return key[index]


def xor_cipher(phrase, key):
    long_key = equal_length(phrase, key)
    cipher_phrase = str()
    for i in range(len(phrase)):
        cipher_phrase += chr(ord(phrase[i]) ^ ord(long_key[i]))
    return cipher_phrase


secret = list(input("input message: "))
password = list(input("input password: "))
encrypt_secret = xor_cipher(secret, password)
decrypt_secret = xor_cipher(encrypt_secret, password)
print("encrypt:", encrypt_secret)
print("decrypt:", decrypt_secret)
