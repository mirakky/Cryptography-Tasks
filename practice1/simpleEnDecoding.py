def forGen(n1, n2):
    while n1 != 0 and n2 != 0:
        if n1 >= n2:
            n1 %= n2
        else:
            n2 %= n1
    return n1 or n2
#функция генерации ключа, делаем более безопасный ключ, такой, что его могут вычислить 2 стороны
#потому что длина строки не меняется после шифрования/асшифрования
def genKey(str):
    global A
    key = sum([i for i in range(len(str))]) % A
    if key == 0 or key == 1:
        key += 2
    while forGen(A, key) != 1:
        key += 1
    return key

def simpleEncode(str):
    global A, key
    res = ''
    for i in range(len(str)):
        res += chr(ord('a') + (((ord(str[i]) - ord('a')) * key) % A))
    print(res)
    #return res


def simpleDecode(str):
    global A, key
    res = ''
    for i in range(len(str)):
        s = (ord(str[i]) - ord('a'))
        while s / key != s // key:
            s += A
        res += chr(ord('a') + s // key)
    print(res)
    #return res


A = 26  # используем латинские символы
str = input()  # вводим строку которую зашифровываем/расшифровываем
key = genKey(str)

simpleEncode(str)
simpleDecode(str)


# def simpleEncode(inp):
    # print('Шифр простой замены. Зашифровка.')
    # d = {'a': 'n', 'b': 'o', 'c': 'p',
    #      'd': 'q', 'e': 'r', 'f': 's', 'g': 't',
    #      'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x',
    #      'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b',
    #      'p': 'c', 'q': 'd', 'r': 'e', 's': 'f',
    #      't': 'g', 'u': 'h', 'v': 'i', 'w': 'j',
    #      'x': 'k', 'y': 'l', 'z': 'm'}
    # res = ''
    # for i in inp:
    #     res += d[i]
    # print(res)
# def simpleDecode(inp):
    # print('Шифр простой замены. Расшифровка.')
    # d = {'n': 'a', 'o': 'b', 'p': 'c',
    #      'q': 'd', 'r': 'e', 's': 'f', 't': 'g',
    #      'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
    #      'y': 'l', 'z': 'm', 'a': 'n', 'b': 'o',
    #      'c': 'p', 'd': 'q', 'e': 'r', 'f': 's',
    #      'g': 't', 'h': 'u', 'i': 'v', 'j': 'w',
    #      'k': 'x', 'l': 'y', 'm': 'z'}
    # res = ''
    # for i in inp:
    #     res += d[i]
    # print(res)