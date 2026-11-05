names = ["Anthony", "Sarah", "Dyrus", "Marcus", "Kevin", "Landon"]
target = input("Enter a name to search for: ")
found = False
for i in range(len(names)):
    if names[i] == target:
        found = True
        break
if found:
    print(f"Found \"{target}\" at index {i}.")
else:
    print(f"\"{target}\" was not found in the list.")
