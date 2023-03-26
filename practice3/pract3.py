import math

'''Функция на проверку взаимной простоты пары чисел'''
def NOD(a,b):
    while(b!=0):
        r = a%b
        a = b
        b = r
    return a

'''Расширенный алгоритм Евклида'''
def advanced_Euclid_algorithm (a,b):
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    while (b!=0):
        q = math.floor(a/b)
        r = a - q*b
        x = x2 - x1*q
        y = y2 - y1*q
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    return y2

'''Проверка числа на простоту'''
def checking_for_a_prime_number(n):
    for a in range(2,20):
        r = pow(a,n-1,n)
        if (r!=1):
            return False
    return True

'''Генерация ключей'''
def key_generation(num):
    p = 0
    q = 0
    for i in range(2**num,2**(num+1)-1):
        if (checking_for_a_prime_number(i)):
            '''Первое простое число'''
            p = i
            break
    for j in range(2**(num+1)-1,2**num,-1):
        if (checking_for_a_prime_number(j)):
            '''Второе простое число'''
            q = j
            break
    '''Модуль алгоритма'''
    n = p*q
    '''Значение функции Эйлера f(n)'''
    f = (p-1)*(q-1)
    e = 0
    for i in range(2,f):
        if (NOD(f,i) == 1):
            '''Экспонента расшифрования'''
            e = i
            break
    '''Экспонента расшифрования'''
    d = advanced_Euclid_algorithm(f,e)%f
    print('Ваша пара открытого ключа:',e,n)
    print("Ваш персональный закрытый ключ:",d)
    return e,n,d

'''Зашифрование'''
def encode(open_text,e,n):
    cipher_text = []
    for m in open_text:
        c = pow(ord(m),e,n)
        cipher_text.append(c)
    return " ".join(str(item) for item in cipher_text)

'''Расшифрование'''
def decode(cipher_text,d,n):
    cipher_text = [int(x) for x in cipher_text.split()]
    open_text = ''
    for c in cipher_text:
        m = chr(pow(int(c),d,n))
        open_text+=m
    return open_text

'''Атака на шифр'''
def attack(cipher_text,e,n):
    cipher_text = [int(x) for x in cipher_text.split()]
    open_text = ''
    for c in cipher_text:
        a = pow(c,e,n)
        b = 0
        while (a!=c):
            b = a
            a = pow(a,e,n)
        open_text+=chr(b)

    return open_text

'''Главная программа'''
print('Введите программе 1, если хотите зашифровать, 2 - расшифровать и 3 - провести атаку на шифр:')
mode = int(input())
if (mode == 1):
    print('Введите программе 1, если хотите сгенерировать ключ, 2 - ввести собственный ключ:')
    cipher_mode = int(input())
    if (cipher_mode == 1):
        print('Введите количетсво бит, в диапозоне которых будет сформирован ключ:')
        z = int(input())
        key = key_generation(z)
        e, n = key[0], key[1]
        print('Введите название файла, в котором хранится ваш текст:')
        name_file = input()
        with open(name_file) as f:
            open_text = f.read()
        open_text = open_text.replace('\n',' ')
        cipher_text = encode(open_text, e, n)
        print('Ваш шифртекст:', cipher_text, sep='\n')
    else:
       print('Введите ваш открытый ключ из пары чисел:')
       e = int(input())
       n = int(input())
       print('Введите название файла, в котором хранится ваш текст:')
       name_file = input()
       with open(name_file) as f:
           open_text = f.read()
       open_text = open_text.replace('\n', ' ')
       cipher_text = encode(open_text, e, n)
       print('Ваш шифртекст:', cipher_text, sep='\n')
elif(mode == 2):
    print('Введите ваш персональный закрытый ключ:')
    d = int(input())
    n = int(input())
    print('Введите название файла, в котором хранится ваш шифртекст:')
    name_file = input()
    with open(name_file) as f:
        cipher_text = f.read()
    cipher_text = cipher_text.replace('\n', ' ')
    print('Ваш открытый текст:', decode(cipher_text, d, n), sep='\n')
else:
    print('Введите открытый ключ из пары чисел:')
    e = int(input())
    n = int(input())
    print('Введите название файла, в котором хранится ваш шифртекст:')
    name_file = input()
    with open(name_file) as f:
        cipher_text = f.read()
    cipher_text = cipher_text.replace('\n', ' ')
    print('Атак прошла успешно! Ваш расшифрованный текст:', attack(cipher_text, e, n), sep='\n')