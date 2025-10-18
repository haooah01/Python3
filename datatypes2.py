"""Illustrates list slicing semantics with various ranges and step values."""

mylist = ["List item 1", 2, 3.14]

if __name__ == "__main__":
    print(mylist[:])
    print(mylist[0:2])
    print(mylist[-3:-1])
    print(mylist[1:])
    print(mylist[::2])
