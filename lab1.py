while True:
    print("\nSimple Messaging App")
    print("1. Send a message")
    print("2. View all messages")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            message = input("Enter your message: ")
            with open("message.txt", "a") as file:
                file.write(message + "\n")
            print("Message saved successfully.")
        except Exception as e:
            print("Error writing to file:", e)

    elif choice == "2":
        try:
            with open("message.txt", "r") as file:
                content = file.read()
                if content:
                    print("\nMessages:\n" + content)
                else:
                    print("No messages found.")
        except Exception as e:
            print("Error reading file:", e)

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
