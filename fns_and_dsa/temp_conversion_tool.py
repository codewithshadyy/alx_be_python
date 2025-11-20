
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(f):
    return (f - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(c):
    return (c * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


temp = input("Enter the temperature to convert: ")


try:
    temp = float(temp)
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "F":
    print(f"{temp}°F is {convert_to_celsius(temp)}°C")
elif unit == "C":
    print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
else:
    print("Invalid unit. Enter 'C' or 'F'.")
