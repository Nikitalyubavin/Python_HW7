# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает
# в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке |
# Ввод:

# пара-ра-рам рам-пам-папам па-ра-па-да

# Вывод:
# Парам пам-пам

input = input("Введите фразу: ")
list1 = input.split()

array = ['а', 'у', 'е', 'ё', 'ы', 'о', 'э', 'я', 'и', 'ю']
list = []
index = 0
while (index < len(list1)):
    sum = 0
    for i in list1[index]:
        if (i in array): sum += 1
    index += 1
    list.append(sum)

if list.count(list[0]) == len(list):
    print("Парам пам-пам!")
else:
    print('Пам парам')