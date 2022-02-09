class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

        @classmethod
        def class_method(cls):
            print(f"Called class_method of {cls}")

        @staticmethod
        def static_method():
            print("Class static_method")

    # instantiation of ClassTest with function instance_method

    test = ClassTest()
    test.instance_method()
    ClassTest.instance_method(test)

    # instantiation of classmethod with funciton class_method
    ClassTest.class_method()

    # class method example
class Book:
    TYPES = ("hardcover", "paperback")

print(Books.TYPES)


#Imports in Python

def divide(dividend, divisor):
    return divdend/divisor


print("mymodule.py: ", __name__)

from mymodule import divide


# Errors in Python

def divide(dividend, divisor):
    if divisor == 0:
        print("Divisor cannot be 0.")
        return

    return dividend/divisor