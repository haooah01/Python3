"""Demonstration of Python's flow control statements: ``if``, ``for``, and ``while``."""

if __name__ == "__main__":
    numbers = range(10)
    print(numbers)

    rangelist = list(numbers)
    print(rangelist)

    for number in range(10):
        if number in (3, 4, 7, 9):
            break
        else:
            continue
    else:
        pass

    if rangelist[1] == 2:
        print("The second item (lists are 0-based) is 2")
    elif rangelist[1] == 3:
        print("The second item (lists are 0-based) is 3")
    else:
        print("Dunno")

    counter = 0
    while rangelist[1] == 1:
        print("We are trapped in an infinite loop!")
        counter += 1
        if counter == 1:
            break
