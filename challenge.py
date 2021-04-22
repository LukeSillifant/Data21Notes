# list = [1, 2]
# i = 1
# sum = 0
# while list[i] < 4000000:
#     list.append(list[i] + list[i-1])
#     if i % 3 == 1:
#         sum += list[i]
#     i += 1
#
# print(sum)
# print(list)
from math import gcd
import math

# maximum = 2000000
# i = 0
# num_list = sorted([2, 3] + list(range(5, maximum, 6)) + list(range(7, maximum, 6)))
# for num in num_list:
#     for x in range(2, int(num**0.5)+1):
#         if num % x == 0:
#             num_list[i] = 0
#     i += 1
#
# print(sum(num_list))
# #142913828922

import math


def func_letters(h, t, u):
    list_unit = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
    list_teen = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    list_ten = [0, 0, 6, 6, 6, 5, 5, 7, 6, 5]
    list_hundred = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print("letters", list_hundred[h], list_ten[t], list_unit[u])
    if t == 1:
        return list_hundred[h]*(list_unit[h]+10) + list_teen[u]
    elif t + u == 0:
        return list_hundred[h] * (list_unit[h] + 7) + list_ten[t] + list_unit[u]
    else:
        return list_hundred[h] * (list_unit[h] + 10) + list_ten[t] + list_unit[u]


sum = 0
number_list = list(range(1, 1000))


for num in number_list:

    hundreds = math.floor(num / 100)
    tens = math.floor(1/10*(num-100*math.floor(num/100)))
    units = (num-100*math.floor(num/100) - 10*math.floor(1/10*(num-100*math.floor(num/100))))
    sum += func_letters(hundreds, tens, units)
#    print("sum", sum)
    print(f" {num} has {func_letters(hundreds, tens, units)} letters")
    print("digits", hundreds, tens, units)

print(sum + 11)
# 20259
