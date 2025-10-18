"""Basic structure of exception handling with try/except/else/finally."""


def some_function():
    try:
        10 / 0
    except ZeroDivisionError:
        print("Oops, invalid.")
    else:
        pass
    finally:
        print("We're done with that.")


if __name__ == "__main__":
    some_function()
