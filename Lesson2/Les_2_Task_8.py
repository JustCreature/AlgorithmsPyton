# Task 8.
# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра,
# которую необходимо посчитать, задаются вводом с клавиатуры.

a = int(input('Введите целое число: '))
x = int(input('Введите число, которое надо посчитать: '))

k = 0

while a > 0:
    b = a//10
    c = a - b*10
    if c == x: k += 1
    a = b

print ('количество цифр:',x,': ', k)