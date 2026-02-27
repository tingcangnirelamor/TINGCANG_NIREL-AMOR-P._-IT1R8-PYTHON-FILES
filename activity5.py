print("Select operation:")
print("\n1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("\nEnter choice: ")

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(f"\n{num1} + {num2} = {num1 + num2}")

elif choice == '2':
    print(f"\n{num1} - {num2} = {num1 - num2}")

elif choice == '3':
    print(f"\n{num1} * {num2} = {num1 * num2}")

elif choice == '4':
    if num2 != 0:
        print(f"\n{num1} / {num2} = {num1 / num2}")
    else:
        print("\nError! Division by zero.")

else:
    print("\nInvalid Input")