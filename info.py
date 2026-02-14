# personal_info.py

# A program that collects and saves user information

# Get information from user
print("=== Personal Info Logger ===")

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

# Create a formatted message
info = f"Name: {name}\nAge: {age}\nCity: {city}\n"

# Save to file
file = open("user_info.txt", "w")
file.write(info)
file.close()

print("\n Information saved to user_info.txt")