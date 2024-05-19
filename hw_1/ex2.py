import wikipedia
import re
import algorithms
from striprtf.striprtf import rtf_to_text


def rtf_read(rtf_file_path):
    with open(rtf_file_path, 'r') as rtf_file:
        return rtf_to_text(rtf_file.read())


# Открываем файл rtf
text = rtf_read('Логика.rtf')
text = re.sub(r'[^а-яА-Я\s]', ' ', text).lower()
text = ' '.join(text.split())

# Скачиваем статью из Википедии
wikipedia.set_lang("ru")
p = wikipedia.page('Логика')
Wiki_content = p.content
text_Wiki = re.sub(r'[^а-яА-Я\s]', ' ', Wiki_content).lower()
text_Wiki = ' '.join(text_Wiki.split())

words = [i for i in text.split(' ')]
words_Wiki = [i for i in text_Wiki.split(' ')]
plagiat = 0
flag = False
k = 0
for i in range(len(words_Wiki) - 2):
    if k != 0:
        k -= 1
        continue
    if not flag:
        substring = ' '.join(words_Wiki[i + j] for j in range(3))
        if algorithms.b_m(text, substring) != 0:
            plagiat += 3
            flag = True
    else:
        k = 1
        while flag:
            substring = ' '.join(words_Wiki[i + j] for j in range(3 + k))
            if algorithms.b_m(text, substring) != 0:
                plagiat += 1
            else:
                flag = False
            k += 1
print(f"Количество плагиата (в % от общего количества символов в реферате): {plagiat / len(words)}")
