# Task 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

while True:
    a = int(input('Введите номер буквы в алфавите: '))
    if a > 0 and a < 27:
        break
    else:
        print('Неправильный ввод, введите снова')
b = a + 96
print (chr(b))
