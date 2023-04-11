"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

lst_word = ['разработка', 'администрирование', 'protocol', 'standard']
lst_encode = []
lst_decode = []


def my_encode(lst_word):
    for line in lst_word:
        k = line.encode('utf-8')
        lst_encode.append(k)
        print(k)


def my_decode(lst_encode):
    for line in lst_encode:
        j = line.decode('utf-8')
        lst_decode.append(j)
        print(j)

print('Вывод преобразованного через encode')
my_encode(lst_word)
print('Вывод преобразованного через decode')
my_decode(lst_encode)