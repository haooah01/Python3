"""Strings in Python can use either single or double quotation marks, and quote
types can be mixed inside one another (e.g., "He said 'hello.'"). Multiline
strings use triple quotes (\"\"\" or '''). Python string objects are Unicode by
default; bytestrings use the ``b`` prefix, such as ``b'Hello \\xce\\xb1'``.

Use the ``%`` operator with a tuple or mapping for legacy interpolation,
``str.format`` for positional or keyword formatting, and f-strings for concise
inline expressions.
"""


class Demo:
    """Simple namespace to mimic the example attribute access."""

    def __init__(self, name: str) -> None:
        self.name = name


if __name__ == "__main__":
    # Show basic string literal variants.
    single_quote = 'He said "hello."'
    double_quote = "She replied 'hi.'"
    multiline = """This is
a multiline
string."""
    bytestring = b"Hello \xce\xb1"

    # Legacy %-formatting with tuple substitution.
    myclass = Demo("Stavros")
    print("Name: %s\nNumber: %s\nString: %s" % (myclass.name, 3, 3 * "-"))

    # Legacy %-formatting with dictionary substitution (note the trailing 's').
    print("This %(verb)s a %(noun)s." % {"noun": "test", "verb": "is"})

    # Modern formatting techniques.
    name = "Stavros"
    print("Hello, {}!".format(name))
    print(f"Hello, {name}!")

    # Display the literal examples so their values are visible.
    print(single_quote)
    print(double_quote)
    print(multiline)
    print(bytestring)
