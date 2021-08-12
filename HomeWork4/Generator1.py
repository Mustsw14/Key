def fibonacci():
    f1 = 1
    f2 = 1
    yield f1
    yield f2
    while True:
        f1 = f2
        f2 = f1 + f2
        yield f2

it = fibonacci()
for i in range(9):
    print(next(it))

