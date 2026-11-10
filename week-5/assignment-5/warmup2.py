num = 0
while True:
    user_input = input("Enter a positive integer: ")
    if user_input.isdigit():
        num = int(user_input)
        if num > 0:
            break
    print("That's not a positive integer. Try again.")
print(f"Got it: {num}")