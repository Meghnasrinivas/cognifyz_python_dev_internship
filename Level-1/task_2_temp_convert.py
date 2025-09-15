# Task-2 

temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C/F): ").strip().upper()

if unit == "C":
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C = {fahrenheit:.2f}°F")

elif unit == "F":
    celsius = (temp - 32) * 5/9
    print(f"{temp}°F = {celsius:.2f}°C")

else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
