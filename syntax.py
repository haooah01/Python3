"""Demonstration of basic arithmetic and string operations from the REPL example."""

myvar = 3
myvar += 2
print(myvar)  # 5

myvar -= 1
print(myvar)  # 4

_ = """This is a multiline comment.
The following lines concatenate the two strings."""

mystring = "Hello"
mystring += " world."
print(mystring)  # Hello world.

# This swaps the variables in one line(!).
# It doesn't violate strong typing because values aren't
# actually being assigned, but new objects are bound to the old names.
myvar, mystring = mystring, myvar
