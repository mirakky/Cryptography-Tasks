import galois

def AfinEncode(str):
    print('Афинный шифр. Зашифровка.')
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    indexes = {}
    for i in range(len(alphabet)):
        indexes[alphabet[i]] = i
    GF = galois.GF(3 ** 3)
    x = GF([i for i in range(1, 27)])
    y = GF([i for i in range(0, 27)])
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    newStr = ''
    for i in str:
        newStr += alphabet[x[a] * y[indexes[i]] + y[b]]
    print(newStr)


def AfinDecode(str):
    print('Афинный шифр. Расшифровка.')
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    indexes = {}
    for i in range(len(alphabet)):
        indexes[alphabet[i]] = i
    GF = galois.GF(3 ** 3)
    x = GF([i for i in range(1, 27)])
    y = GF([i for i in range(0, 27)])
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    newStr = ''
    for i in str:
        newStr += alphabet[(y[indexes[i]] - y[b]) * (x[a] ** -1)]
    print(newStr)


AfinEncode(input('Введите текст: '))
AfinDecode('pyhgmzp')
