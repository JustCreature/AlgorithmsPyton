import random as rm

# a. случайное целое число,
cr = input('Введите диапазон целых чисел в формате x,y: ').split(',')
print(rm.randint(int(cr[0]),int(cr[1])))

# b. случайное вещественное число
cr = input('Введите диапазон вещественных чисел в формате x,y: ').split(',')
print(rm.uniform(float(cr[0]),float(cr[1])))

# c. случайный символ.
cr = input('Введите диапазон символов от a до z в формате x,y: ').split(',')
c = ord(cr[0])
d = ord(cr[1])
f = rm.randint(c,d)
print(chr(f))

