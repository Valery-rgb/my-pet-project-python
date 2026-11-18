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
        if len(to_do) == 0:
            print("No tasks yet")
        elif len(to_do) > 0:
            for i, task in enumerate(to_do, start=1):
                print(i, task)

    elif choice == "3":
        number = input("What number do you want delete?: ")

    elif choice == "4":
        break
    else:
        print("Wrong choice")
