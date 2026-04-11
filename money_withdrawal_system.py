balance = 20000

while True:
    print("Money Withdrawal System")
    print("\n1. Withdaw Money")
    print("2. Check Balance")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter amount to withdraw: "))

            if amount > balance:
                print("Insufficient funds!")

                while True:
                    print("\nWhat would you like to do?")
                    print("1. Try Again")
                    print("2. Check Balance")
                    print("3. Exit")

                    option = input("Enter your choice: ")

                    if option == "1":
                        break
                    elif option == "2":
                        print(f"Current balance: {balance}")
                    elif option == "3":
                        print("Thank you for using the system!")
                        exit()
                    else:
                        print("Invalid option. Try again.")

            elif amount <= 0:
                print("Invalid amount. Please enter a positive number.")

            else:
                balance -= amount
                print(f"Withdrawal successful! Remaining balance: {balance}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == "2":
        print(f"Your current balance is: {balance}")

    elif choice == "3":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please select 1-3.")