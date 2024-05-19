import zlib


# метод деления
def division_hash(data, size):
    s = 0
    for i in data:
        s += ord(i)
    return s % size


# метод crc32 встроенным методом
def crc(data):
    return zlib.crc32(data.encode())


# метод crc32 стандартным методом
def crc32(data):
    text = data.encode()
    crc = 0xFFFFFFFF
    poly = 0xEDB88320
    for byte in text:
        crc ^= byte
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ poly
            else:
                crc >>= 1
    return crc ^ 0xFFFFFFFF


# метод crc32 табличным методом
def generate_crc32_table():
    table = []
    poly = 0xEDB88320
    for i in range(256):
        crc = i
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ poly
            else:
                crc >>= 1
        table.append(crc)
    return table


def crc32_table_method(data):
    buf = data.encode()
    crc = 0xFFFFFFFF
    for byte in buf:
        crc = (crc >> 8) ^ crc32_table[(crc ^ byte) & 0xFF]
    return crc ^ 0xFFFFFFFF


crc32_table = generate_crc32_table()

# пример
data = input("Введите текст для хэширования:\n")
print("Хэш методом деления: ", division_hash(data, 11))
print("Хэш CRC-32 встроенным методом: ", crc32(data))
print("Хэш CRC-32 стандартным методом: ", crc(data))
print("Хэш CRC-32 табличным методом: ", crc32_table_method(data))