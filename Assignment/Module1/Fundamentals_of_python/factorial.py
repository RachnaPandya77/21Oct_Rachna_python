# Write a Python program to get the Factorial number of given number


n = int(input("Enter a number: "))#5
fact = 1

for i in range(1, n+1):
    fact*=i

print("factorial: ", end="")
print(fact)

