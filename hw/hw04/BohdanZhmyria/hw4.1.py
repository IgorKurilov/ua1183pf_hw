C = int(input("What is the temperature today in Celsius? "))
F = (C * 9/5) + 32
if C > -273.15:
    print("The temperature in Fahrenheit is", F)
else:
    print("Error: Temperature below absolute zero (-273.15°C)")