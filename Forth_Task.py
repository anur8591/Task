print("🌡️ Temperature Converter 🌡️")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = int(input("enter 1 or 2: "))

temp = float(input("enter the temperature: "))

if choice == 1:
    fahre = (temp * 9/5) + 32
    print(f"{temp}°C = {fahre:.2f}°F")
elif choice == 2:
    cels = (temp - 32) * 5/9
    print(f"{temp}°F = {cels:.2f}°C")
else:
    print("Invalid choice. please enter 1 or 2")