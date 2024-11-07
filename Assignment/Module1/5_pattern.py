"""Print this pattern using nested for loop
*
**
***
****
*****               """

for i in range(0,6):
    for j in range(i):
        print("*",end="")
    print(" ")
