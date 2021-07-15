from datetime import  datetime

TodoList = []
prompt1= ('List all incomplete todo items')
prompt2 =('List incomplete todo items due today')
prompt3 = ('Add a todo Item')
prompt4 = ('Complete a to do item')
prompt5 = ('Quit')
prompt6 = ('Enter Item description')
prompt7 = ('Enter due date/time (MM/DD/YYYY):')
prompt8 = ('Enter Item to Complete')



user_input  = ""
numbers = 1
while user_input != 5:
    Store_Todo_OnebyOne = {}
    print(f"Main menu: \n1 {prompt1},\n2 {prompt2},\n3 {prompt3},\n4 {prompt4},\n5 {prompt5}")
    user_input = int(input("Enter your choice>"))
    if user_input == 3:
        print("")
        print("")
        todolist_input_item = input(prompt6)
        todolist_input_date = input(prompt7)
        format = "%Y-%m-%d %H:%M:%S"
        todolist_input_date = datetime.strptime(todolist_input_date,format)
        Store_Todo_OnebyOne['number'] = numbers
        Store_Todo_OnebyOne['description'] = todolist_input_item
        Store_Todo_OnebyOne['due date/time'] = todolist_input_date
        Store_Todo_OnebyOne['completed'] = 0
        numbers = numbers +1
        TodoList.append(Store_Todo_OnebyOne)
        print("")
        print("")

        continue
    if user_input == 5:
        print('Bye!')
        break
    if user_input == 1:
        TodoList_temp = []
        i = len(TodoList)
        while i > 0:
            for Store_Todo_OnebyOne in TodoList:
                if Store_Todo_OnebyOne['completed'] == 0:
                    '''
                    TodoList_temp.append(Store_Todo_OnebyOne)
                    '''
                    print(f"{Store_Todo_OnebyOne['description']} due {Store_Todo_OnebyOne['due date/time']} \n")
                    i = i -1
    if user_input == 4:
        TodoList_temp = []
        m = 0
        i = len(TodoList)
        while i > 0:
            for Store_Todo_OnebyOne in TodoList:
                if Store_Todo_OnebyOne['completed'] == 0:
                    TodoList_temp.append(Store_Todo_OnebyOne)
                    i = i - 1
        j = len(TodoList_temp)
        while j > 0:
            for Store_Todo_OnebyOne in TodoList_temp:
                print(f"{m} {Store_Todo_OnebyOne['description']} due {Store_Todo_OnebyOne['due date/time']} \n")
                m = m + 1
                j = j -1
        user_input_1 = int(input(prompt8))
        save_number = TodoList_temp[user_input_1]
        print(TodoList_temp[user_input_1:user_input_1+1])
        for item in TodoList_temp[user_input_1:user_input_1+1]:
            save_number = item['number']
        d = next(item for item in TodoList if item['number'] == save_number)
        d['completed'] = 1

    if user_input == 2:
        i = len(TodoList)
        CurrentDate = datetime.date.today()
        while i > 0:
            for Store_Todo_OnebyOne in TodoList:
                if Store_Todo_OnebyOne['due date/time'] == CurrentDate:
                    i = i - 1














