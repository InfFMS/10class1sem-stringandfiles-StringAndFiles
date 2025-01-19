# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.
from string import punctuation

with open('task5.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    text = text.replace('\n', ' ')
    for symbol in punctuation:
        text = text.replace(symbol, '')
    words = text.split()
    longest_word = max(words, key=len)
    print(f'Самое длинное слово: {longest_word}')
    print(f'Его длина: {len(longest_word)}')
    with open('task5_upd.txt', 'w', encoding='utf-8') as f:
        f.write(f'Самое длинное слово: {longest_word}\n')
        f.write(f'Его длина: {len(longest_word)}\n')
