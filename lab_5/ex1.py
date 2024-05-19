def brackets(s):
    cnt, n = 0, len(s)
    for i in range(n):
        if s[i] == ')':
            cnt -= 1
        else:
            cnt += 1
        if cnt < 0:
            return False, i + 1
    if cnt == 0:
        return True, 0
    else:
        return False, -1


while True:
    s = input("Введите последовательность скобок: ")
    x = brackets(s)
    if x[0]:
        print("Все верно!")
    else:
        if x[1] == -1:
            print(f"Скобочная последовательность неверна! Количество '(' и ')' не совпадает!")
        else:
            print(f"Скобочная последовательность неверна! Нарушение в {x[1]} элементе!")
