import galois

def AfinRecEncode(str):
    print('Афинный рекурентный шифр. Зашифровка.')
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    indexes = {}
    for i in range(len(alphabet)):
        indexes[alphabet[i]] = i
    GF = galois.GF(3 ** 3)
    x = GF([i for i in range(1, 27)])
    y = GF([i for i in range(0, 27)])
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    a2 = int(input('Введите a2: '))
    b2 = int(input('Введите b2: '))
    newStr = ''
    newStr += alphabet[x[a] * y[indexes[str[0]]] + y[b]]
    newStr += alphabet[x[a2] * y[indexes[str[1]]] + y[b2]]
    for i in str[2::]:
        a2, a = x[a] * x[a2], a2
        b2, b = y[b] + y[b2], b2
        newStr += alphabet[x[a2] * y[indexes[i]] + y[b2]]
    print(newStr)

def AfinRecDecode(str):
    print('Афинный рекурентный шифр. Расшифровка.')
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    indexes = {}
    for i in range(len(alphabet)):
        indexes[alphabet[i]] = i
    GF = galois.GF(3 ** 3)
    x = GF([i for i in range(1, 27)])
    y = GF([i for i in range(0, 27)])
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    a2 = int(input('Введите a2: '))
    b2 = int(input('Введите b2: '))
    newStr = ''
    newStr += alphabet[(y[indexes[str[0]]] - y[b]) * (x[a] ** -1)]
    newStr += alphabet[(y[indexes[str[1]]] - y[b2]) * (x[a2] ** -1)]
    for i in str[2::]:
        a2, a = x[a] * x[a2], a2
        b2, b = y[b] + y[b2], b2
        newStr += alphabet[(y[indexes[i]] - y[b2]) * (x[a2] ** -1)]
    print(newStr)

AfinRecEncode('apple')
AfinRecDecode('hloriqkurdp')

