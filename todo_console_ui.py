from datetime import datetime

TodoList = []
while (1): # Infinite loop to print the menu again and again till quit option is not choosen
    print("Main Menu : ")
    print("1. List all incomplete todo items")
    print("2. List incomplete todo items due today")
    print("3. Add a todo item")
    print("4. Complete a todo item")
    print("5. Quit")
    choice = int(input("Enter your choice > "))
    if choice == 1:
        print("\nIncomplete items:")
        for item in TodoList:
            print(f"\t{item[0]} due {str(item[1])}")
    elif choice == 2:
        print("\nIncomplete items due today:")
        DateCurrent = datetime.now()
        for item in TodoList:
            if item[1].date() == DateCurrent.date():
                print(f"\t{item[0]} due {str(item[1])}")
    elif choice == 3:
        desc = input("\nEnter item description : ")
        datedue = input("Enter due date/time (MM/DD/YYYY hh:mm) : ")
        format = "%m/%d/%Y %H:%M"
        datedue = datetime.strptime(datedue, format)
        tpl = (desc, datedue)
        print(tpl)
        TodoList.append(tpl)
    elif choice == 4:
        if len(TodoList) != 0:
            print("\nIncomplete items:")
            x = 0
            for tpl in TodoList:
                print(f"\t{x}) {tpl[0]} due {str(tpl[1])}")
                x += 1
            delete = int(input("\nEnter item to complete : "))
            del TodoList[delete]
        else:
            print("No incomplete todo items available.")
    elif choice == 5:
        print("Bye!")
        exit()
    else:
        print("\n")
