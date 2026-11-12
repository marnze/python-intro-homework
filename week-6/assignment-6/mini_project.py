numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def find_min(numbers):
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
    return min

def find_max(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max

def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

def bubble_sort(numbers):
    sorted = numbers.copy()
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(sorted)-1):
            if sorted[i] > sorted[i + 1]:
                sorted[i], sorted[i + 1] = sorted[i + 1], sorted[i]
                swapped = True
    return sorted

def show_menu():
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    return input("Choose an option (1-5): ")

def main():
    while True:
        option = show_menu()
        match option:
            case '1':
                print(f"\nThe smallest value in {numbers} is:\n{find_min(numbers)}\n")

            case '2':
                print(f"\nThe largest value in {numbers} is:\n{find_max(numbers)}\n") 

            case '3':
                while True:
                    target = input("\nEnter the number you want: ")
                    if target.isdigit():
                        target = int(target)
                        break
                    print("Invalid number. Try again.")
                index = search(numbers, target)
                if index != -1:
                    print(f"{target} was found at index {index} of {numbers}\n")
                else:
                    print(f"{target} was not found.\n")

            case '4':
                print(f"\n{bubble_sort(numbers)}\n")

            case '5':
                print("\nThank you for using the Number Cruncher. Goodbye.")
                break

            case _:
                print("\nInvalid option. Try again\n")

main()