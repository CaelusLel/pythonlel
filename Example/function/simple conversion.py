
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit + 459.67) * 5/9
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin * 9/5) - 459.67
    return fahrenheit

# Test the functions
celsius = 25
converted_fahrenheit = celsius_to_fahrenheit(celsius)
converted_kelvin = celsius_to_kelvin(celsius)
print(f"{celsius} degrees Celsius is equal to {converted_fahrenheit} degrees Fahrenheit.")
print(f"{celsius} degrees Celsius is equal to {converted_kelvin} Kelvin.")

fahrenheit = 77
converted_celsius = fahrenheit_to_celsius(fahrenheit)
converted_kelvin = fahrenheit_to_kelvin(fahrenheit)
print(f"{fahrenheit} degrees Fahrenheit is equal to {converted_celsius} degrees Celsius.")
print(f"{fahrenheit} degrees Fahrenheit is equal to {converted_kelvin} Kelvin.")

kelvin = 298.15
converted_celsius = kelvin_to_celsius(kelvin)
converted_fahrenheit = kelvin_to_fahrenheit(kelvin)
print(f"{kelvin} Kelvin is equal to {converted_celsius} degrees Celsius.")
print(f"{kelvin} Kelvin is equal to {converted_fahrenheit} degrees Fahrenheit.")
