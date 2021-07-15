from name_function import getname

print("Enter q at anytime to quit")
while True:
    first = input("Give me your first name")
    if first == 'q':
        break
    last = input("Give me your last name")
    if last == 'q':
        break
    formattedname = getname(first,last)
    print(f" Neatly formatted name = {formattedname}")
