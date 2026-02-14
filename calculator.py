# calculator.py

# A calculator that logs all calculations
print("=== Calculator with History ===")

# Get numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero"

# Display results
print(f"\nResults:")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")

# Save to history (append mode)
history = open("calc_history.txt", "a")  # "a" = append
history.write(f"{num1} + {num2} = {addition}\n")
history.close()