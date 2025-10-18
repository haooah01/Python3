"""Examples demonstrating class instantiation, attribute sharing, and inheritance."""


class MyClass(object):
    common = 10

    def __init__(self):
        self.myvariable = 3

    def myfunction(self, arg1, arg2):
        return self.myvariable


class OtherClass(MyClass):
    def __init__(self, arg1):
        self.myvariable = 3
        print(arg1)


if __name__ == "__main__":
    classinstance = MyClass()
    print(classinstance.myfunction(1, 2))

    classinstance2 = MyClass()
    print(classinstance.common)
    print(classinstance2.common)

    MyClass.common = 30
    print(classinstance.common)
    print(classinstance2.common)

    classinstance.common = 10
    print(classinstance.common)
    print(classinstance2.common)

    MyClass.common = 50
    print(classinstance.common)
    print(classinstance2.common)

    classinstance = OtherClass("hello")
    print(classinstance.myfunction(1, 2))

    classinstance.test = 10
    print(classinstance.test)
