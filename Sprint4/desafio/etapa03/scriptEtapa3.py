import hashlib

while True:
    data = input("Digite uma string: ")

    result = hashlib.sha1(data.encode())

    print("O hash SHA1 da string é : ", end ="")
    print(result.hexdigest())
