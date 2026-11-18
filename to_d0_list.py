to_do = []

while True:
    print("1 - Add ")
    print("2 - Show ")
    print("3 - Delete ")
    print("4 - Exit from menu ")

    choice = input("Please choose a number: ")

    if choice == "1":
        task = input("Enter a task: ")
        to_do.append(task)
        print(f"Added: {task}")

    elif choice == "2":
        print("Show ")
    elif choice == "3":
        print("Delete ")
    elif choice == "4":
        break
    else:
        print("Wrong choice")
