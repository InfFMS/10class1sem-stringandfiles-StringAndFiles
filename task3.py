# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
from string import punctuation

with open('task3.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    for symbol in punctuation:
        text = text.replace(symbol, ' ')
    words = text.split()
    for i in range(len(words)):
        words[i] = words[i].lower()
    unique_words = sorted(list(set(words)))
    with open('unique_words.txt', 'w', encoding='utf-8') as f_unique_words:
        for word in unique_words:
            count = words.count(word)
            f_unique_words.write(f'{word}: {count}\n')
