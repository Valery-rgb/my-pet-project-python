to_do = []

while True:
    print("1 - Add ")
    print("2 - Show ")
    print("3 - Delete ")
    print("4 - Exit from menu ")

    choice = input("Please choose a number: ")

    if choice == "1":
        print("To do: ")
    elif choice == "2":
        print("Show ")
    elif choice == "3":
        print("Delete ")
    elif choice == "4":
        break
    else:
        print("Wrong choice")
