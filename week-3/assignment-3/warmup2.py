age = int(input("Enter your age: "))

print("You are a ", end="")
if age >= 0 and age <= 12:
    print("Child")
elif age >= 13 and age <= 17:
    print("Teen")
elif age >= 18 and age <= 64:
    print("Adult")
elif age >= 65:
    print("Senior")
else:
    "Idea"