from secrets import token_bytes

def endecode():
    print('Шифр AES.')
    c = input('Выберите зашифрование или расшифрование - 1 или 2: ')
    if c == '1':
        key = token_bytes(16)
        d = open('opentext.txt', 'r')
        data = d.read()
        d.close()
        encrypt(b'2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c', data.encode("utf-8"))
    elif c == '2':
        ct = open('ciphertext.txt', 'rb')
        ciphertext = ct.read()
        k = open('key.txt', 'rb')
        key = k.read()

        ct.close()
        k.close()
        decrypt(key, ciphertext)
    else:
        print('Упс, похоже вы ввели что-то не так, попробуйте сначала :)')

def StateBreak16(s):
    all = []
    for i in range(len(s) // 16):
        b = s[i * 16: i * 16 + 16]
        mesh = [[], [], [], []]
        for i in range(4):
            for j in range(4):
                mesh[i].append(b[i + j * 4])
        all.append(mesh)
    return all

# Значения элементов Sbox представлены в шестнадцатеричной системе счисления.
SubBytes = [
    [int('63', 16), int('7c', 16), int('77', 16), int('7b', 16), int('f2', 16), int('6b', 16), int('6f', 16),
     int('c5', 16), int('30', 16), int('01', 16), int('67', 16), int('2b', 16), int('fe', 16), int('d7', 16),
     int('ab', 16), int('76', 16)],
    [int('ca', 16), int('82', 16), int('c9', 16), int('7d', 16), int('fa', 16), int('59', 16), int('47', 16),
     int('f0', 16), int('ad', 16), int('d4', 16), int('a2', 16), int('af', 16), int('9c', 16), int('a4', 16),
     int('72', 16), int('c0', 16)],
    [int('b7', 16), int('fd', 16), int('93', 16), int('26', 16), int('36', 16), int('3f', 16), int('f7', 16),
     int('cc', 16), int('34', 16), int('a5', 16), int('e5', 16), int('f1', 16), int('71', 16), int('d8', 16),
     int('31', 16), int('15', 16)],
    [int('04', 16), int('c7', 16), int('23', 16), int('c3', 16), int('18', 16), int('96', 16), int('05', 16),
     int('9a', 16), int('07', 16), int('12', 16), int('80', 16), int('e2', 16), int('eb', 16), int('27', 16),
     int('b2', 16), int('75', 16)],
    [int('09', 16), int('83', 16), int('2c', 16), int('1a', 16), int('1b', 16), int('6e', 16), int('5a', 16),
     int('a0', 16), int('52', 16), int('3b', 16), int('d6', 16), int('b3', 16), int('29', 16), int('e3', 16),
     int('2f', 16), int('84', 16)],
    [int('53', 16), int('d1', 16), int('00', 16), int('ed', 16), int('20', 16), int('fc', 16), int('b1', 16),
     int('5b', 16), int('6a', 16), int('cb', 16), int('be', 16), int('39', 16), int('4a', 16), int('4c', 16),
     int('58', 16), int('cf', 16)],
    [int('d0', 16), int('ef', 16), int('aa', 16), int('fb', 16), int('43', 16), int('4d', 16), int('33', 16),
     int('85', 16), int('45', 16), int('f9', 16), int('02', 16), int('7f', 16), int('50', 16), int('3c', 16),
     int('9f', 16), int('a8', 16)],
    [int('51', 16), int('a3', 16), int('40', 16), int('8f', 16), int('92', 16), int('9d', 16), int('38', 16),
     int('f5', 16), int('bc', 16), int('b6', 16), int('da', 16), int('21', 16), int('10', 16), int('ff', 16),
     int('f3', 16), int('d2', 16)],
    [int('cd', 16), int('0c', 16), int('13', 16), int('ec', 16), int('5f', 16), int('97', 16), int('44', 16),
     int('17', 16), int('c4', 16), int('a7', 16), int('7e', 16), int('3d', 16), int('64', 16), int('5d', 16),
     int('19', 16), int('73', 16)],
    [int('60', 16), int('81', 16), int('4f', 16), int('dc', 16), int('22', 16), int('2a', 16), int('90', 16),
     int('88', 16), int('46', 16), int('ee', 16), int('b8', 16), int('14', 16), int('de', 16), int('5e', 16),
     int('0b', 16), int('db', 16)],
    [int('e0', 16), int('32', 16), int('3a', 16), int('0a', 16), int('49', 16), int('06', 16), int('24', 16),
     int('5c', 16), int('c2', 16), int('d3', 16), int('ac', 16), int('62', 16), int('91', 16), int('95', 16),
     int('e4', 16), int('79', 16)],
    [int('e7', 16), int('c8', 16), int('37', 16), int('6d', 16), int('8d', 16), int('d5', 16), int('4e', 16),
     int('a9', 16), int('6c', 16), int('56', 16), int('f4', 16), int('ea', 16), int('65', 16), int('7a', 16),
     int('ae', 16), int('08', 16)],
    [int('ba', 16), int('78', 16), int('25', 16), int('2e', 16), int('1c', 16), int('a6', 16), int('b4', 16),
     int('c6', 16), int('e8', 16), int('dd', 16), int('74', 16), int('1f', 16), int('4b', 16), int('bd', 16),
     int('8b', 16), int('8a', 16)],
    [int('70', 16), int('3e', 16), int('b5', 16), int('66', 16), int('48', 16), int('03', 16), int('f6', 16),
     int('0e', 16), int('61', 16), int('35', 16), int('57', 16), int('b9', 16), int('86', 16), int('c1', 16),
     int('1d', 16), int('9e', 16)],
    [int('e1', 16), int('f8', 16), int('98', 16), int('11', 16), int('69', 16), int('d9', 16), int('8e', 16),
     int('94', 16), int('9b', 16), int('1e', 16), int('87', 16), int('e9', 16), int('ce', 16), int('55', 16),
     int('28', 16), int('df', 16)],
    [int('8c', 16), int('a1', 16), int('89', 16), int('0d', 16), int('bf', 16), int('e6', 16), int('42', 16),
     int('68', 16), int('41', 16), int('99', 16), int('2d', 16), int('0f', 16), int('b0', 16), int('54', 16),
     int('bb', 16), int('16', 16)]
]

InvSubBytes = [
    [int('52', 16), int('09', 16), int('6a', 16), int('d5', 16), int('30', 16), int('36', 16), int('a5', 16),
     int('38', 16), int('bf', 16), int('40', 16), int('a3', 16), int('9e', 16), int('81', 16), int('f3', 16),
     int('d7', 16), int('fb', 16)],
    [int('7c', 16), int('e3', 16), int('39', 16), int('82', 16), int('9b', 16), int('2f', 16), int('ff', 16),
     int('87', 16), int('34', 16), int('8e', 16), int('43', 16), int('44', 16), int('c4', 16), int('de', 16),
     int('e9', 16), int('cb', 16)],
    [int('54', 16), int('7b', 16), int('94', 16), int('32', 16), int('a6', 16), int('c2', 16), int('23', 16),
     int('3d', 16), int('ee', 16), int('4c', 16), int('95', 16), int('0b', 16), int('42', 16), int('fa', 16),
     int('c3', 16), int('4e', 16)],
    [int('08', 16), int('2e', 16), int('a1', 16), int('66', 16), int('28', 16), int('d9', 16), int('24', 16),
     int('b2', 16), int('76', 16), int('5b', 16), int('a2', 16), int('49', 16), int('6d', 16), int('8b', 16),
     int('d1', 16), int('25', 16)],
    [int('72', 16), int('f8', 16), int('f6', 16), int('64', 16), int('86', 16), int('68', 16), int('98', 16),
     int('16', 16), int('d4', 16), int('a4', 16), int('5c', 16), int('cc', 16), int('5d', 16), int('65', 16),
     int('b6', 16), int('92', 16)],
    [int('6c', 16), int('70', 16), int('48', 16), int('50', 16), int('fd', 16), int('ed', 16), int('b9', 16),
     int('da', 16), int('5e', 16), int('15', 16), int('46', 16), int('57', 16), int('a7', 16), int('8d', 16),
     int('9d', 16), int('84', 16)],
    [int('90', 16), int('d8', 16), int('ab', 16), int('00', 16), int('8c', 16), int('bc', 16), int('d3', 16),
     int('0a', 16), int('f7', 16), int('e4', 16), int('58', 16), int('05', 16), int('b8', 16), int('b3', 16),
     int('45', 16), int('06', 16)],
    [int('d0', 16), int('2c', 16), int('1e', 16), int('8f', 16), int('ca', 16), int('3f', 16), int('0f', 16),
     int('02', 16), int('c1', 16), int('af', 16), int('bd', 16), int('03', 16), int('01', 16), int('13', 16),
     int('8a', 16), int('6b', 16)],
    [int('3a', 16), int('91', 16), int('11', 16), int('41', 16), int('4f', 16), int('67', 16), int('dc', 16),
     int('ea', 16), int('97', 16), int('f2', 16), int('cf', 16), int('ce', 16), int('f0', 16), int('b4', 16),
     int('e6', 16), int('73', 16)],
    [int('96', 16), int('ac', 16), int('74', 16), int('22', 16), int('e7', 16), int('ad', 16), int('35', 16),
     int('85', 16), int('e2', 16), int('f9', 16), int('37', 16), int('e8', 16), int('1c', 16), int('75', 16),
     int('df', 16), int('6e', 16)],
    [int('47', 16), int('f1', 16), int('1a', 16), int('71', 16), int('1d', 16), int('29', 16), int('c5', 16),
     int('89', 16), int('6f', 16), int('b7', 16), int('62', 16), int('0e', 16), int('aa', 16), int('18', 16),
     int('be', 16), int('1b', 16)],
    [int('fc', 16), int('56', 16), int('3e', 16), int('4b', 16), int('c6', 16), int('d2', 16), int('79', 16),
     int('20', 16), int('9a', 16), int('db', 16), int('c0', 16), int('fe', 16), int('78', 16), int('cd', 16),
     int('5a', 16), int('f4', 16)],
    [int('1f', 16), int('dd', 16), int('a8', 16), int('33', 16), int('88', 16), int('07', 16), int('c7', 16),
     int('31', 16), int('b1', 16), int('12', 16), int('10', 16), int('59', 16), int('27', 16), int('80', 16),
     int('ec', 16), int('5f', 16)],
    [int('60', 16), int('51', 16), int('7f', 16), int('a9', 16), int('19', 16), int('b5', 16), int('4a', 16),
     int('0d', 16), int('2d', 16), int('e5', 16), int('7a', 16), int('9f', 16), int('93', 16), int('c9', 16),
     int('9c', 16), int('ef', 16)],
    [int('a0', 16), int('e0', 16), int('3b', 16), int('4d', 16), int('ae', 16), int('2a', 16), int('f5', 16),
     int('b0', 16), int('c8', 16), int('eb', 16), int('bb', 16), int('3c', 16), int('83', 16), int('53', 16),
     int('99', 16), int('61', 16)],
    [int('17', 16), int('2b', 16), int('04', 16), int('7e', 16), int('ba', 16), int('77', 16), int('d6', 16),
     int('26', 16), int('e1', 16), int('69', 16), int('14', 16), int('63', 16), int('55', 16), int('21', 16),
     int('0c', 16), int('7d', 16)]
]

# Функции для доступа к позиции для SubBytes
# Берём наиболее значимый фрагмент в качестве строки и наименее значимый фрагмент в качестве столбцов:
def SearchSub(byte):
    x = byte >> 4
    y = byte & 15
    return SubBytes[x][y]
# Для InvSubBytes
def InvSearchSub(byte):
    x = byte >> 4
    y = byte & 15
    return InvSubBytes[x][y]


def KeyExpansion(key, rounds):
    # Значения в шестнадцатиричной сс
    Rcon = [[1, 0, 0, 0]]

    for _ in range(1, rounds):
        Rcon.append([Rcon[-1][0] * 2, 0, 0, 0])
        if Rcon[-1][0] > 0x80:
            Rcon[-1][0] ^= 0x11b

    key_mesh = StateBreak16(key)[0]

    for round in range(rounds):
        last_column = [row[-1] for row in key_mesh]
        last_column_rotate_step = shiftRowLeft(last_column)
        last_column_sbox_step = [SearchSub(b) for b in last_column_rotate_step]
        last_column_rcon_step = [last_column_sbox_step[i] ^ Rcon[round][i] for i in range(len(last_column_rotate_step))]

        for r in range(4):
            key_mesh[r] += bytes([last_column_rcon_step[r] ^ key_mesh[r][round * 4]])

        # Three more columns to go
        for i in range(len(key_mesh)):
            for j in range(1, 4):
                key_mesh[i] += bytes([key_mesh[i][round * 4 + j] ^ key_mesh[i][round * 4 + j + 3]])

    return key_mesh


def shiftRowLeft(row, n=1):
    return row[n:] + row[:n]


def multiplication2(v):
    s = v << 1
    s &= 0xff
    if (v & 128) != 0:
        s = s ^ 0x1b
    return s


def multiplication3(v):
    return multiplication2(v) ^ v

def MixColumn(column):
    r = [
        multiplication2(column[0]) ^ multiplication3(column[1]) ^ column[2] ^ column[3],
        multiplication2(column[1]) ^ multiplication3(column[2]) ^ column[3] ^ column[0],
        multiplication2(column[2]) ^ multiplication3(column[3]) ^ column[0] ^ column[1],
        multiplication2(column[3]) ^ multiplication3(column[0]) ^ column[1] ^ column[2],
    ]
    return r

def MixColumns(mesh):
    new_mesh = [[], [], [], []]
    for i in range(4):
        col = [mesh[j][i] for j in range(4)]
        col = MixColumn(col)
        for i in range(4):
            new_mesh[i].append(col[i])
    return new_mesh

# Добавляем подключ или просто xor побайтовый массив. Алгоритм дозаполнения KeySchedule :
def RefillKey(block_mesh, key_mesh):
    r = []

    # 4 ряда в сетке
    for i in range(4):
        r.append([])
        # 4 значения в каждой строке
        for j in range(4):
            r[-1].append(block_mesh[i][j] ^ key_mesh[i][j])
    return r

# Ключ извлечения для раунда:
def KeyExtractRound(KeyExp, round):
    return [row[round * 4: round * 4 + 4] for row in KeyExp]


def encrypt(key, data):
    # Сначала нам нужно дополнить данные символом \x00 и разбить их на блоки по 16
    compl = bytes(16 - len(data) % 16)

    if len(compl) != 16:
        data += compl
    meshes = StateBreak16(data)

        # Теперь нам нужно расширить ключ для нескольких раундов
    KeyExp = KeyExpansion(key, 11)

    # Применяем оригинальный ключ к блокам перед началом раундов и начинаем работать с целыми числами:
    temp_meshes = []
    round_key = KeyExtractRound(KeyExp, 0)

    for mesh in meshes:
        temp_meshes.append(RefillKey(mesh, round_key))

    meshes = temp_meshes

    # Основная часть алгоритма:
    for round in range(1, 10):
        temp_meshes = []

        for mesh in meshes:
            sub_bytes_step = [[SearchSub(val) for val in row] for row in mesh]
            shift_rows_step = [shiftRowLeft(sub_bytes_step[i], i) for i in range(4)]
            mix_column_step = MixColumns(shift_rows_step)
            round_key = KeyExtractRound(KeyExp, round)
            add_sub_key_step = RefillKey(mix_column_step, round_key)
            temp_meshes.append(add_sub_key_step)

        meshes = temp_meshes

    # Финальный раунд без миксования колонок
    temp_meshes = []
    round_key = KeyExtractRound(KeyExp, 10)

    for mesh in meshes:
        sub_bytes_step = [[SearchSub(val) for val in row] for row in mesh]
        shift_rows_step = [shiftRowLeft(sub_bytes_step[i], i) for i in range(4)]
        add_sub_key_step = RefillKey(shift_rows_step, round_key)
        temp_meshes.append(add_sub_key_step)

    meshes = temp_meshes

    # Воссоздаём данные в один поток перед их возвратом
    int_stream = []
    for mesh in meshes:
        for column in range(4):
            for row in range(4):
                int_stream.append(mesh[row][column])
                print(hex(mesh[row][column]), end=' ')
            print()
        print()
    print(bytes(int_stream))
    s = open('ciphertext.txt', 'wb')

    s.write(bytes(int_stream))
    s.close()
    #print(f'Ваш шифртекст находится в файле: {bytes(int_stream)}')
    print(f'Ваш шифртекст находится в файле: {"ciphertext.txt"}')

    k = open('key.txt', 'wb')
    ky = k.write(key)
    k.close()

def decrypt(key, data):
    meshes = StateBreak16(data)
    KeyExp = KeyExpansion(key, 11)
    round_key = KeyExtractRound(KeyExp, 10)

    # Отменяем финальный раунд
    temp_meshes = []

    for mesh in meshes:
        add_sub_key_step = RefillKey(mesh, round_key)
        shift_rows_step = [shiftRowLeft(add_sub_key_step[i], -1 * i) for i in range(4)]
        sub_bytes_step = [[InvSearchSub(val) for val in row] for row in shift_rows_step]
        temp_meshes.append(sub_bytes_step)

    meshes = temp_meshes

    for round in range(9, 0, -1):
        temp_meshes = []

        for mesh in meshes:
            round_key = KeyExtractRound(KeyExp, round)
            add_sub_key_step = RefillKey(mesh, round_key)

            # Выполнение смешивания столбцов три раза равно использованию обратной матрицы
            mix_column_step = MixColumns(add_sub_key_step)
            mix_column_step = MixColumns(mix_column_step)
            mix_column_step = MixColumns(mix_column_step)
            shift_rows_step = [shiftRowLeft(mix_column_step[i], -1 * i) for i in range(4)]
            sub_bytes_step = [[InvSearchSub(val) for val in row] for row in shift_rows_step]
            temp_meshes.append(sub_bytes_step)

        meshes = temp_meshes
        temp_meshes = []

    # Изменение первого дополнительного ключа добавления (Раундовый ключ)
    round_key = KeyExtractRound(KeyExp, 0)

    for mesh in meshes:
        temp_meshes.append(RefillKey(mesh, round_key))

    meshes = temp_meshes

    # Преобразуем нашу сетку в байты
    int_stream = []
    for mesh in meshes:
        for column in range(4):
            for row in range(4):
                int_stream.append(mesh[row][column])
    out = []
    for i in range(len(int_stream)):
        if int_stream[i] == 0:
            break
        else:
            out.append(int_stream[i])

    #print(f'Opentext: {bytes(out).decode("utf-8")}')
    print(f'Ваш открытый текст находится в файле: {"opentext.txt"}')
    return bytes(int_stream)

endecode()