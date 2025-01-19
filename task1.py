# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
with open('task1.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    total_lines = len(lines)
    total_words = sum(len(line.split()) if '—' not in line else len(line.split()) - line.count('—') for line in lines)
    total_chars = sum(len(line) for line in lines)
    print(f'Total lines: {total_lines}')
    print(f'Total words: {total_words}')
    print(f'Total characters: {total_chars}')
