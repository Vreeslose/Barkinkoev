sample 
Чтобы выбрать какое-то количество элементов из набора данных можно воспользоваться функцией sample(х, k)

import random
a = [10, 12, 13, 15, 14, 16]
a = random.sample(a, 4)
print(a)

> [10, 12, 11, 14]

shuffle 
Перемешать элементы набора данных можно с помощью функции shuffle(x[, random])

import random

a = ["1", "2", "3", "4"]
random.shuffle(seq)
print(seq)

> ['3', '1', '4', '2']

choices 
С помощью функции choices можно выбрать 1 или несколько элементов из набора данных.
random import
a = [20, 30, 40, 50 ,60, 70, 80, 90]
 a = random.choices(a, k=5)
 print(a)

> [50, 20, 60, 40, 90]

uniform 
Сгенерировать число с плавающей точкой можно с помощью функции uniform(a, b)

import random
a = random.uniform(1.1, 10.5)
print(a)

> 10.320165816501492

random 
Функция random() выдает вещественные числа, в диапазоне [0.0, 1.0) (включая 0.0, но не включая 1.0).

import random

a = random.random()
print(a)

> 0.47673250896173136

randrange 
В функцию randrange() передают три целых числа:

import random

a = random.randrange(1, 100, 2)
print(a)

> 43

randint 
Функция randint(a, b) получает на вход два целых числа и возвращает случайное значение из диапазона [a, b] (a и b входят в этот диапазон).

import random

a = random.randint(0, 125)
print(a)

> 113
