# Write a Python program to check if a person is eligible to donate bloodusing a nested if

age = int(input("Enter your age: "))
healthcondition = input("Enter Health condition(Good or Poor): ")

if age >= 18 and age <=60:
    if healthcondition == "good":
        print("You can donate blood")
    else:
        print("You can not donate blood because of 'poor health'")

else:
    print("You are not eligible to donate blood")

