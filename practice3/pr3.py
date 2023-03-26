import math

def endecrypt():
    choose = input('Выберите зашифрование или расшифрование или произвести атаку - 1 или 2 или 3: ')
    if (choose == '1'):
        keymode = input('Выберите 1 - сгенерировать ключ или 2 - ввести собственный ключ: ')
        if (keymode == '1'):
            bit = int(input('Введите диапазон бит для генерации ключа: '))
            key = KeyGen(bit)
            e, n = key[0], key[1]
            with open('opentext.txt', 'r', encoding='utf-8') as f:
                opentext = f.read()
            opentext = opentext.replace('\n', ' ')
            ciphertext = encrypt(opentext, e, n)
            print('Ciphertext: ', ciphertext, sep='\n')
        elif (keymode == '2'):
            print('Введите открытый ключ из пары чисел:')
            e = int(input('1-й: '))
            n = int(input('2-й: '))

            with open('opentext.txt', 'r', encoding='utf-8') as f:
                opentext = f.read()
            opentext = opentext.replace('\n', ' ')
            ciphertext = encrypt(opentext, e, n)
            print('Ciphertext: ', ciphertext, sep='\n')
        else:
            print('Упс, похоже вы ввели что-то не так, попробуйте сначала :)')
    elif (choose == '2'):
        print('Введите открытый ключ из пары чисел:')
        d = int(input('1-й: '))
        n = int(input('2-й: '))

        with open('ciphertext.txt', 'r', encoding='utf-8') as f:
            ciphertext = f.read()
        ciphertext = ciphertext.replace('\n', ' ')
        print('Opentext: ', decrypt(ciphertext, d, n), sep='\n')
    elif (choose == '3'):
        print('Введите открытый ключ из пары чисел:')
        e = int(input('1-й: '))
        n = int(input('2-й: '))

        with open('ciphertext.txt', 'r', encoding='utf-8') as f:
            ciphertext = f.read()
        ciphertext = ciphertext.replace('\n', ' ')
        d, n = attack(e, n)
        print(f'Закрытый секретный ключ: ({d}, {n})')
        result = decrypt(ciphertext, e, n)
        print('The attack was successful! Your decrypted text is: ' + result)
    else:
        print('Упс, похоже вы ввели что-то не так, попробуйте сначала :)')

# Функция для проверки взаимной простоты пары чисел (Наибольший общий делитель - Greatest common divisor)
def GCD(a, b):
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a


# Расширенный алгоритм Евклида
def EucAlg(a, b):
    x1 = 0
    x2 = 1

    y1 = 1
    y2 = 0
    while (b != 0):
        q = math.floor(a / b)
        r = a - q * b
        x = x2 - x1 * q
        y = y2 - y1 * q

        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y

    return y2

# Проверям число на простоту
def NumCheck(n):
    for a in range(2, 20):
        r = pow(a, n - 1, n)
        if (r != 1):
            return False
    return True


# Генерируем ключ
def KeyGen(n):
    p = 0
    q = 0
    for i in range(2 ** n, 2 ** (n + 1) - 1):
        if (NumCheck(i)):
            p = i
            break
    for j in range(2 ** (n + 1) - 1, 2 ** n, -1):
        if (NumCheck(j)):
            q = j
            break
    n = p * q
    # Функция Эйлера F(n)
    F = (p - 1) * (q - 1)
    e = 0
    for i in range(2, F):
        if (GCD(F, i) == 1):
            # e шифрования
            e = i
            break
    # e расшифрования (экспонента зашифрования)
    d = EucAlg(F, e) % F
    print(f'Пара открытого ключа: {e, n}', )
    print(f'Закрытый секретный ключ: {d}')
    return e, n, d


# Проводим шифровку
def encrypt(opentext, e, n):
    ciphertext = []
    for i in opentext:
        ciphertext.append(pow(ord(i), e, n))
    ct = ' '.join(str(item) for item in ciphertext)

    with open('ciphertext.txt', 'w', encoding='utf-8') as l:
        l.write(ct)
    l.close()
    return ct

# Проводим расшифровку
def decrypt(ciphertext, d, n):
    ciphertext = [int(x) for x in ciphertext.split()]
    ot = ''
    for c in ciphertext:
        a = pow(c, d, n)
        b = 0
        while (a != c):
            b = a
            a = pow(a, d, n)
        ot += chr(b)
    with open('plaintext.txt', 'w', encoding='utf-8') as l:
        l.write(ot)
    return ot

def AlgPollard(n):
    """
    Алгоритм Полларда для нахождения простых множителей числа n

    :param n: число, для которого нужно найти простые множители

    :return: простой множитель числа n
    """
    d = n
    a, b = 2, 2

    while d <= 1 or d >= n:
        a = (a ** 2 + 1) % n
        b = (b ** 2 + 1) % n
        b = (b ** 2 + 1) % n

        d = math.gcd(a - b, n)

    return d


def foundD(euler, e):
    """
    Нахождение d по формуле d * e = 1 mod euler

    :param euler: значение функции Эйлера
    :param e: значение открытой экспоненты

    :return: значение закрытой экспоненты
    """
    d = gcdE(euler, e)[2]
    if d < 0: d += euler

    return d


def gcdE(num1, num2):
    """
    Расширенный алгоритм Евклида

    :param num1: первое число
    :param num2: второе число
    :return: результат расширенного алгоритма Евклида
    """
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = gcdE(num2 % num1, num1)

    return (div, y - (num2 // num1) * x, x)


def attack(e, n):
    """
    :param e: открытая экспонента
    :param n: n закрытого ключа

    :return: закрытый ключ
    """
    p = AlgPollard(n)
    q = n // p
    euler = (p - 1) * (q - 1)

    d = foundD(euler, e)
    return (d, n)

endecrypt()
