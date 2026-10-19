num = int(input("Enter a number: "))

# Check sign
if num < 0:
    print(f"{num} is negative.")
elif num > 0: 
    print(f"{num} is positive.")
else:
    print(f"{num} is zero.")

# Check parity
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")