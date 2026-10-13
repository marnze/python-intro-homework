def convert_temp(temp, unit):
    match unit.upper():
        case 'C':
            return (temp - 32) * 5 / 9
        case 'F':
            return (temp * 9 / 5) + 32
        case _:
            return "Invalid unit"
temp_f = float(input("Enter a temperature in Fahrenheit: "))
print(f"{temp_f:.1f}°F is {convert_temp(temp_f, 'C'):.1f}°C")