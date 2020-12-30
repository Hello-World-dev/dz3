# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    temp = 0
    if arg1 > arg2:
        temp = arg2
        arg2 = arg1
        arg1 = temp

    if arg2 > arg3:
        temp = arg3
        arg3 = arg2
        arg2 = temp

    return arg2 + arg3

# ---------------------------------
print(my_func(1, 8, 3))
