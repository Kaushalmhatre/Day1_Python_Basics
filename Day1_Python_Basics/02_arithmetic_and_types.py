num1 = float(input("Enter the first number: "))  
num2 = float(input("Enter the second number: "))  

print("\n--- Results ---")
print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")

if num2 != 0:
    print(f"Division: {num1 / num2}")
else:
    print("Division: Cannot divide by zero")


whole_number = int(input("\nEnter a whole number: "))
decimal_number = float(input("Enter a decimal number: "))
user_text = str(input("Enter some text: "))
is_positive = whole_number > 0  # bool

print("\n--- Converted Values and Types ---")
print(f"Integer: {whole_number} ({type(whole_number).__name__})")
print(f"Float: {decimal_number} ({type(decimal_number).__name__})")
print(f"String: {user_text} ({type(user_text).__name__})")
print(f"Is the whole number positive? {is_positive} ({type(is_positive).__name__})")
