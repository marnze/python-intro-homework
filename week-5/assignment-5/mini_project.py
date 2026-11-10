numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    option = input("Choose an option (1-5): ")

    match option:
        case '1':
            min = numbers[0]
            for num in numbers:
                if num < min:
                    min = num
            print(f"\nThe smallest value in {numbers} is:\n{min}\n")

        case '2':
            max = numbers[0]
            for num in numbers:
                if num > max:
                    max = num
            print(f"\nThe largest value in {numbers} is:\n{max}\n") 

        case '3':
            while True:
                target = input("\nEnter the number you want: ")
                if target.isdigit():
                    target = int(target)
                    break
                print("Invalid number. Try again.")
            found = False
            for i in range(len(numbers)):
                if numbers[i] == target:
                    found = True
                    break
            if found:
                print(f"{target} was found at index {i} of {numbers}\n")
            else:
                print(f"{target} was not found.\n")

        case '4':
            swapped = True
            while swapped:
                swapped = False
                for i in range(len(numbers)-1):
                    if numbers[i] > numbers[i + 1]:
                        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                        swapped = True
            print(f"\n{numbers}\n")

        case '5':
            print("\nThank you for using the Number Cruncher. Goodbye.")
            break

        case _:
            print("\nInvalid option. Try again\n")


