"""Miscellaneous Python language features: chained comparisons, deletions,
list comprehensions, any/sum, and global variable behavior."""


number = 5


def myfunc():
    print(number)


def anotherfunc():
    print(number)
    number = 3  # noqa: F841


def yetanotherfunc():
    global number
    number = 3


if __name__ == "__main__":
    a = 2
    print(1 < a < 3)

    lst1 = [1, 2, 3]
    lst2 = [3, 4, 5]
    print([x * y for x in lst1 for y in lst2])
    print([x for x in lst1 if 4 > x > 1])

    print(any([i % 3 for i in [3, 3, 4, 4, 3]]))
    print(sum(1 for i in [3, 3, 4, 4, 3] if i == 4))

    del lst1[0]
    print(lst1)
    del lst1

    myfunc()

    try:
        anotherfunc()
    except UnboundLocalError as exc:
        print(f"Caught expected exception: {exc}")

    yetanotherfunc()
    print(number)
