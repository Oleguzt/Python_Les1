# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print('Введите трехзначное число: ')
num = input()
sum = int(num[0]) + int(num[1]) + int(num[2])
print(f"{num} -> {sum} ({num[0]} + {num[1]} + {num[2]})")