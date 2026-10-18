celsius = float(input("Degrees in Celsius: "))

# Standard degrees conversion in the the world
fahrenheit = round(celsius * 9 / 5 + 32, 2)
kelvin = round(celsius + 273.15, 2)

print(f"Degrees in Fahrenheit: {fahrenheit} °F")
print(f"Degrees in Kelvin: {kelvin} K")