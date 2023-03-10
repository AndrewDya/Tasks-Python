# Задача №1. За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?

# n = 700
# m = 750
# days = (m - 1) // n + 1
# print("Через " + str(days) + " дней, проедет " +
#       str(m) + " километров")

# Задача №2: Найдите сумму цифр трехзначного числа.

# a = int(input("Введите трёхзначное число: "))
# if 99 < a < 1000:
#     res = int(str(a)[0]) + int(str(a)[1]) + int(str(a)[2])
#     print("Сумма чисел трёхзначного числа: " + str(res))
# else:
#     print("Прочтите условие внимательнее")

# Задача №3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты дляних новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.

# var1 = 20
# var2 = 21
# var3 = 22
# parts = 0
# if var1 % 2 == 1:
#     parts += 1
# if var2 % 2 == 1:
#     parts += 1
# if var3 % 2 == 1:
#     parts += 1
# parts = parts + (var1 // 2) + (var2 // 2) + (var3 // 2)
# print("Как минимум понадобится " + str(parts) + " парты")

# Задача №4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# Задача №5. Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда,
# а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер. Витя сел в i-й вагон
# от головы поезда и обнаружил, что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.

# Задача №6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# a = int(input("Введите номер билета: "))
# if 99_999 < a < 1_000_000:
#     if int(str(a)[0]) + int(str(a)[1]) + int(str(a)[2]) == int(str(a)[3]) + int(str(a)[4]) + int(str(a)[5]):
#         print("Вы счастливчик!")
#     else:
#         print("Повезёт в другой раз")
# else:
#     print("Прочтите условие внимательнее")

# Задача №7. Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным,
# то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.

# Задача №8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# Задача №9. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N(произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

# Задача №10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые
# нужно перевернуть.

# Задача №11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n) = A.
# Если А не является числом Фибоначчи, выведите число - 1.

# Задача №12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных
# числа X и Y(X, Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# Задача №13. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней(1 ≤ N ≤ 100). В следующих строках располагается N целых чисел. Каждое число – среднесуточная
# температура в соответствующий день. Температуры

# Задача №14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# Задача №15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему! Пользователь вводит
# одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
