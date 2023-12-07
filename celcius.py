def celsius_to_fahrenheit(celsius):
    return (celsius * 9)/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return [(fahrenheit - 32) * 5]/9

try:
    choice = input("Enter 'C' to convert from Celsius to Fahrenheit, or 'F' to convert from Fahrenheit to Celsius: ").upper()

    if choice == 'C':
        celsius_temperature = float(input("Enter temperature in Celsius: "))
        converted_fahrenheit = celsius_to_fahrenheit(celsius_temperature)
        print(f"{celsius_temperature}°C is equal to {converted_fahrenheit:.2f}°F")
    elif choice == 'F':
        fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))
        converted_celsius = fahrenheit_to_celsius(fahrenheit_temperature)
        print(f"{fahrenheit_temperature}°F is equal to {converted_celsius:.2f}°C")
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")

except ValueError:
    print("Invalid input. Please enter a valid temperature value.")
