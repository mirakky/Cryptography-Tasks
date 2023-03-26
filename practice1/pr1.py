import galois

def endecode():
    c = input('Выберите зашифрование или расшифрование - 1 или 2: ')
    if c == '1':
        inp = input('Введите строку: ')
        s = input('Выберите шифр: \n'
                  'Шифр простой замены - 1 \n'
                  'Аффинный шифр - 2 \n'
                  'Аффинный рекуррентный шифр - 3 \n')
        if s == '1':
            simpleEncode(inp)
        elif s == '2':
            AffinEncode(inp)
        elif s == '3':
            AffinRecEncode(inp)
        else:
            print('Упс, похоже вы ввели что-то не так, попробуйте сначала :)')
    elif c == '2':
        inp = input('Введите строку: ')
        s = input('Выберите шифр: \n'
                  'Шифр простой замены - 1 \n'
                  'Аффинный шифр - 2 \n'
                  'Аффинный рекуррентный шифр - 3 \n')
        if s == '1':
            simpleDecode(inp)
        elif s == '2':
            AffinDecode(inp)
        elif s == '3':
            AffinRecDecode(inp)
        else:
            print('Упс, похоже вы ввели что-то не так, попробуйте сначала :)')
    else:
        print('Упс, похоже вы ввели что-то не так, попробуйте сначала :)')


def forGen(n1, n2):
    while n1 != 0 and n2 != 0:
        if n1 >= n2:
            n1 %= n2
        else:
            n2 %= n1
    return n1 or n2


def genKey(inp):
    K = sum([i for i in range(len(inp))]) % 26
    if K == 0 or K == 1:
        K += 2
    while forGen(26, K) != 1:
        K += 1
    return K


def simpleEncode(inp):
    print('Шифр простой замены. Зашифровка.')
    K = genKey(inp)
    res = ''
    for i in range(len(inp)):
        res += chr(ord('a') + (((ord(inp[i]) - ord('a')) * K) % 26))
    print(res)


def simpleDecode(inp):
    print('Шифр простой замены. Расшифровка.')
    K = genKey(inp)
    res = ''
    for i in range(len(inp)):
        s = (ord(inp[i]) - ord('a'))
        while s / K != s // K:
            s += 26
        res += chr(ord('a') + s // K)
    print(res)


def AffinEncode(inp):
    print('Аффинный шифр. Зашифровка.')
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    indexes = {}
    for i in range(len(alphabet)):
        indexes[alphabet[i]] = i

    GF = galois.GF(3 ** 3)
    x = GF([i for i in range(1, len(alphabet))])
    y = GF([i for i in range(0, len(alphabet))])
    print(GF.properties)
    a1 = int(input('Введите a1: '))
    b1 = int(input('Введите b1: '))
    newStr = ''
    for i in inp:
        newStr += alphabet[x[a1] * y[indexes[i]] + y[b1]]
    print(newStr)


def AffinDecode(inp):
    print('Аффинный шифр. Расшифровка.')
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    indexes = {}
    for i in range(len(alphabet)):
        indexes[alphabet[i]] = i

    GF = galois.GF(3 ** 3)
    x = GF([i for i in range(1, len(alphabet))])
    y = GF([i for i in range(0, len(alphabet))])
    print(GF.properties)
    a1 = int(input('Введите a1: '))
    b1 = int(input('Введите b1: '))
    newStr = ''
    for i in inp:
        newStr += alphabet[(y[indexes[i]] - y[b1]) * (x[a1] ** -1)]
    print(newStr)


def AffinRecEncode(inp):
    print('Аффинный рекуррентный шифр. Зашифровка.')
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    indexes = {}
    for i in range(len(alphabet)):
        indexes[alphabet[i]] = i

    GF = galois.GF(3 ** 3)
    x = GF([i for i in range(1, len(alphabet))])
    y = GF([i for i in range(0, len(alphabet))])

    a1 = int(input('Введите a1: '))
    b1 = int(input('Введите b1: '))
    a2 = int(input('Введите a2: '))
    b2 = int(input('Введите b2: '))
    newStr = ''

    newStr += alphabet[x[a1] * y[indexes[inp[0]]] + y[b1]]
    newStr += alphabet[x[a2] * y[indexes[inp[1]]] + y[b2]]
    for i in inp[2::]:
        a2, a1 = x[a1] * x[a2], a2
        b2, b1 = y[b1] + y[b2], b2
        newStr += alphabet[x[a2] * y[indexes[i]] + y[b2]]
    print(newStr)


def AffinRecDecode(inp):
    print('Аффинный рекуррентный шифр. Расшифровка.')
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    indexes = {}
    for i in range(len(alphabet)):
        indexes[alphabet[i]] = i

    GF = galois.GF(3 ** 3)
    x = GF([i for i in range(1, len(alphabet))])
    y = GF([i for i in range(0, len(alphabet))])

    a1 = int(input('Введите a1: '))
    b1 = int(input('Введите b1: '))
    a2 = int(input('Введите a2: '))
    b2 = int(input('Введите b2: '))
    newStr = ''

    newStr += alphabet[(y[indexes[inp[0]]] - y[b1]) * (x[a1] ** -1)]
    newStr += alphabet[(y[indexes[inp[1]]] - y[b2]) * (x[a2] ** -1)]
    for i in inp[2::]:
        a2, a1 = x[a1] * x[a2], a2
        b2, b1 = y[b1] + y[b2], b2
        newStr += alphabet[(y[indexes[i]] - y[b2]) * (x[a2] ** -1)]
    print(newStr)
endecode()
