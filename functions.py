"""Examples of defining and using functions, defaults, and lambda expressions."""

funcvar = lambda x: x + 1  # Same as def funcvar(x): return x + 1


def passing_example(a_list, an_int=2, a_string="A default string"):
    """Append to the provided list, shadow the int, and return a tuple."""
    a_list.append("A new item")
    an_int = 4
    return a_list, an_int, a_string


if __name__ == "__main__":
    print(funcvar(1))

    my_list = [1, 2, 3]
    my_int = 10

    print(passing_example(my_list, my_int))
    print(my_list)
    print(my_int)
