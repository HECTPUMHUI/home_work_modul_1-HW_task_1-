num_1 = 23
num_2 = 12
sign = '/'

if sign == '+':
    print(num_1 + num_2)
elif sign == '-':
    print(num_1 - num_2)

elif sign == '*':
    print(num_1 * num_2)
elif sign == '/':
    if num_2 != 0:
        print(num_1 / num_2)
    else:
        print("Zero division error")