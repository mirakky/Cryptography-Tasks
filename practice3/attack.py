import math


def pollard(n):
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

def crack(e, n):
    """
    Функция для взлома RSA

    :param e: открытая экспонента
    :param n: n закрытого ключа

    :return: закрытый ключ
    """

    p = pollard(n)
    q = n // p
    euler = (p - 1) * (q - 1)

    d = foundD(euler, e)

    return (d, n)



# # realise attack on rsa
# def crack(e, n):
#     # find p and q
#     p, q = find_pq(n)
#     # find d
#     d = find_d(e, p, q)
#     # return d
#     return d


if __name__ == "__main__":
    print(crack(159531117506814229037, 1097578570310371255535445065193282061318689904047539))