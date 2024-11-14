print("----------------Grade Managemnet System----------------")

python = int(input("Enter marks for python: "))
Html = int(input("Enter marks for Html: "))
javascript = int(input("Enter marks for javascript: "))
c_lang = int(input("Enter marks for c_lang: "))
print("\n")

if python >= 40 and Html >= 40 and javascript >= 40 and c_lang >= 40:

    total = python + Html + javascript + c_lang
    print("Total : ",total)
    
    PR = total / 4
    print("Percentage: ", PR)

#(95>a+, 85>a, 75>b, 65>c, 55>pass)
    if PR >= 95:
        print("Grade: A+")
    elif PR >= 85:
        print("Grade: A")
    elif PR >= 75:
        print("Grade : B")
    elif PR >= 65:
        print("Grade: C")
    elif PR >= 55:
        print("Result: PASS")
else:
    print("Result: FAIL")

