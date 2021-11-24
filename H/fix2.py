sample 
Чтобы выбрать какое-то количество элементов из набора данных можно воспользоваться функцией sample(х, k)

import random
seq = [10, 12, 13, 15, 14, 16]
random_seq = random.sample(seq, 4)
print(random_seq)

> [10, 12, 11, 14]

shuffle 
Перемешать элементы набора данных можно с помощью функции shuffle(x[, random])

import random

seq = ["a", "b", "c", "d"]
random.shuffle(seq)
print(seq)

> ['c', 'a', 'd', 'b']

choices 
С помощью функции choices можно выбрать 1 или несколько элементов из набора данных.

import random

seq = [1, 2, 3, 4, 5, 6]
random_elements = random.choices(seq, k=4)
print(random_elements)

> [5, 1, 1, 5]

uniform 
Сгенерировать число с плавающей точкой можно с помощью функции uniform(a, b)

import random
random_number = random.uniform(1.1, 10.5)
print(random_number)

> 10.320165816501492

random 
Функция random() выдает вещественные числа, в диапазоне [0.0, 1.0) (включая 0.0, но не включая 1.0).

import random

random_number = random.random()
print(random_number)

> 0.47673250896173136

randrange 
В функцию randrange() передают три целых числа:

import random

random_number = random.randrange(1, 100, 2)
print(random_number)

> 43

randint 
Функция randint(a, b) получает на вход два целых числа и возвращает случайное значение из диапазона [a, b] (a и b входят в этот диапазон).

import random

random_number = random.randint(0, 125)
print(random_number)

> 113
