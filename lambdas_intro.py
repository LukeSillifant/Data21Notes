import math
# def addition(num1, num2):
#     return num1 + num2
#
#
# add = lambda num1, num2: num1 + num2
#
#
# print(addition(1, 2))
# print(add(1, 2))
savings = [234, 555, 674, 78]

# int(math.log10(i)))

def bonus_func(savings_list):
    return [round(1.1*i, 2) for i in savings_list]


bonus_lambda = list(map(lambda x: round(1.1*x, 2), savings))


print(bonus_func(savings))
print(bonus_lambda)
