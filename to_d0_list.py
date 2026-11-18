to_do = []

while True:
    print()
    print("-" * 20)
    print("1 - Add ")
    print("2 - Show ")
    print("3- Mark as done")
    print("4 - Delete ")
    print("5 - Exit from menu ")

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
        try:
            if len(to_do) == 0:
                print("You dont have any tasks for today")
            elif len(to_do) > 0:
                num = int(
                    input("What number of task you want to mark as a done?: "))
                to_do[-1] = " ✅" + to_do[-1]
                print(to_do)
        except ValueError:
            print("Please enter a number!")
    elif choice == "4":
        try:
            if len(to_do) == 0:
                print("You dont have any tasks to delete")
            elif len(to_do) > 0:
                number = int(input("What number do you want delete?: "))
                if 1 <= number <= len(to_do):
                    removed = to_do.pop(number - 1)
                    print(f"Deleted:{removed}")
                else:
                    print("Wrong number")
        except ValueError:
            print("Please enter a number!")

    elif choice == "5":
        break
    else:
        print("Wrong choice")
