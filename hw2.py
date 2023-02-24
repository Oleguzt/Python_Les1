# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# если получается некорректное разделение - напечатать "Неверное S"

print('Введите количество журавликов: ')
s = int(input())
if s % 3 != 0 or s // 3 % 2 !=0:
     print('Неверное S')
else:
    print(f"{s} -> {s//3//2}  {s//3*2}  {s//3//2}")