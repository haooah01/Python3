"""Help in Python is always available right in the interpreter.
If you want to know how an object works, all you have to do is call help(<object>)!
Also useful are dir(), which shows you all the object's methods,
and <object>.__doc__, which shows you its documentation string:

>>> help(5)
Help on int object:
(etc etc)

>>> dir(5)
['__abs__', '__add__', ...]

>>> abs.__doc__
'abs(number) -> number

Return the absolute value of the argument.
"""


if __name__ == "__main__":
    print(__doc__)
