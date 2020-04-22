"""
Task 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* задача считается решённой, если в коде использована функция вычисления хеша (hash(), sha1() или любая другая из модуля hashlib)
"""

import hashlib


#  функция принимает на вход строку, состоящую только из маленьких латинских букв, и возвращает количество различных подстрок с использованием хеш-функции, не включаем пустую строку и строку целиком
def count_eq_str(x):
    x = str(x).lower()
    length = len(x)
    c = set()

    for i in range(length + 1):
        for j in range(i + 1, length + 1):
            h = hashlib.sha1(x[i:j].encode('utf-8')).hexdigest()
            c.add(h)
            # print(x[i:j])
            k = len(c) - 1
    return k


s1 = input('Введите основную строку: ')
print('Количество различных подстрок равно: ', count_eq_str(s1))