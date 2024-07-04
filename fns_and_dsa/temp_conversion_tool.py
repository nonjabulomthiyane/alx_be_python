# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius using global conversion factor
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit using global conversion factor
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    while True:
        try:
            temperature = float(input("Enter the temperature: "))
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
            continue
        
        unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'F':
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temperature:.2f}°C.")
        elif unit == 'C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temperature:.2f}°F.")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            continue
        
        break

if __name__ == "__main__":
    main()
