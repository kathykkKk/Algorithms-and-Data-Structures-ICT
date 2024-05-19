import pandas as pd


df = pd.read_excel('students.xlsx')
data_array = df.values
questions = data_array[0][1:]
data_array = data_array[1:]
characteristics = {}
for i in data_array:
    s = ''
    for j in range(1, 7):
        if i[j] == 'да':
            s += '1'
        else:
            s += '0'
    if s in characteristics.keys():
        print(f"Студент {characteristics[s]} и {i[0]} имеют совпадающие ключи!")
    else:
        characteristics[s] = i[0]
"""
for i in characteristics:
    print(f"{i} --> {characteristics[i]}")
"""
print(characteristics['100000'])
mas = [i for i in characteristics.keys()]
cnt = 0
while len(mas) > 1:
    print(mas)
    mas_temp = []
    answer = '1' if 'да' in input(f">> {questions[cnt]}\n>> ").lower() else '0'
    for i in mas:
        if i[cnt] == answer:
            mas_temp.append(i)
    mas = mas_temp
    cnt += 1

print(f"Загаданный студент: {characteristics[mas[0]]}.")
