"""Examples demonstrating Python's core data types and mutations."""

sample = [1, ["another", "list"], ("a", "tuple")]
mylist = ["List item 1", 2, 3.14]
mylist[0] = "List item 1 again"  # Update the first element.
mylist[-1] = 3.21  # Update the last element.

mydict = {"Key 1": "Value 1", 2: 3, "pi": 3.14}
mydict["pi"] = 3.15  # Change a dictionary value.

mytuple = (1, 2, 3)
myfunction = len

if __name__ == "__main__":
    print(myfunction(mylist))
