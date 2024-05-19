import time


def fibonacci():
    mas = [0, 1, 1]
    while len(mas) <= 500:
        mas.append(mas[len(mas) - 1] + mas[len(mas) - 2])
    return ''.join(map(str, mas))


# наивный
def naive(line, substring):
    cnt = 0
    m = len(substring)
    n = len(line)
    for j in range(n - m + 1):
        flag = 0
        for i in range(m):
            if substring[i] != line[j + i]:
                flag = 1
                break
        if flag == 0:
            cnt += 1
    return cnt


# Рабина-Карпа
def r_k(line, substring):
    n, m = len(line), len(substring)
    cnt, h_substring = 0, hash(substring)
    for j in range(n - m + 1):
        line_part = line[j:j + m]
        if len(line_part) == m:
            h_line_part = hash(line_part)
            if h_substring == h_line_part:
                flag = 0
                for i in range(m):
                    if substring[i] != line[j + i]:
                        flag = 1
                        break
                if flag == 0:
                    cnt += 1
    return cnt


# Рабина-Карпа с самостоятельным подсчетом хэша
def r_k_own_hash(line, substring):
    n, m = len(line), len(substring)
    numbers_for_symbols = {}
    for i in range(n):
        if line[i] not in line[:i]:
            numbers_for_symbols[line[i]] = i
    cnt, h_substring, x = 0, 0, len(numbers_for_symbols)
    for k in range(m):
        h_substring += numbers_for_symbols[substring[k]] * x ** (m - 1 - k)
    h_line_part = 0
    for j in range(n - m + 1):
        line_part = line[j:j + m]
        if len(line_part) == m:
            if j == 0:
                for k in range(m):
                    h_line_part += numbers_for_symbols[line_part[k]] * x ** (m - 1 - k)
            else:
                h_line_part = (h_line_part - numbers_for_symbols[line[j - 1]] * x ** (m - 1)) * x \
                              + numbers_for_symbols[line_part[m - 1]]
            if h_substring == h_line_part:
                flag = 0
                for i in range(m):
                    if substring[i] != line[j + i]:
                        flag = 1
                        break
                if flag == 0:
                    cnt += 1
    return cnt


# Бойера-Мура
def b_m(line, substring):
    m = len(substring)
    d = {}
    for i in range(m - 2, -1, -1):
        if substring[i] not in d:
            d[substring[i]] = m - i - 1
    if substring[m - 1] not in d:
        d[substring[m - 1]] = m
    d['*'] = m
    cnt = 0
    n = len(line)
    i = m - 1
    while i < n:
        k = 0
        for j in range(m - 1, -1, -1):
            if line[i - k] != substring[j]:
                if j == m - 1:
                    off = d[line[i]] if d.get(line[i], False) else d['*']
                else:
                    off = d[substring[j]]
                i += off
                break
            k += 1
            if j == 0:
                cnt += 1
                i += 1
    return cnt


# Кнута-Морриса-Пратта
def k_m_p(line, substring):
    m = len(substring)
    pi = []
    for i in range(1, m + 1):
        s = substring[:i]
        p = 0
        for j in range(1, i):
            if s[:j] == s[i - j:]:
                p = j
        pi.append(p)
    n = len(line)
    i, j, cnt = 0, 0, 0
    while i < n:
        if line[i] == substring[j]:
            i += 1
            j += 1
            if j == m:
                cnt += 1
                j = pi[j - 1]
        else:
            if j != 0:
                j = pi[j - 1]
            else:
                i += 1

    return cnt


start = time.time()
max_cnt = 0
for i in range(10, 100):
    max_cnt = max(max_cnt, naive(fibonacci(), str(i)))
end = time.time() - start
print('Наивный', max_cnt, end)

start = time.time()
max_cnt = 0
for i in range(10, 100):
    max_cnt = max(max_cnt, r_k(fibonacci(), str(i)))
end = time.time() - start
print('Рабина-Карпа', max_cnt, end)

start = time.time()
max_cnt = 0
for i in range(10, 100):
    max_cnt = max(max_cnt, r_k_own_hash(fibonacci(), str(i)))
end = time.time() - start
print('Рабина-Карпа (самостоятельный подсчет хэша)', max_cnt, end)

start = time.time()
max_cnt = 0
for i in range(10, 100):
    max_cnt = max(max_cnt, b_m(fibonacci(), str(i)))
end = time.time() - start
print('Бойера-Мура', max_cnt, end)

start = time.time()
max_cnt = 0
for i in range(10, 100):
    max_cnt = max(max_cnt, k_m_p(fibonacci(), str(i)))
end = time.time() - start
print('Кнута-Морриса-Пратта', max_cnt, end)
