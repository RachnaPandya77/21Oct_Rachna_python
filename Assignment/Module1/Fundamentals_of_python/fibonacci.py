# Write a Python program to get the Fibonacci series of given range.

n = int(input("Enter a number: "))#5
fact = 1

for i in range(1, n+1):
    fact*=i  #fact=1
    
print("factorial: ", end="")
print(fact)