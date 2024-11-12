#  Write a Python program to check if a number is prime using if_else

num = 11
j = 0 # for count no. of factor

if num > 1:
    for i in range(1, num+1):
        if num % i == 0:
            j += 1

    if j == 2:
        print('prime')

    else:
        print('not prime')