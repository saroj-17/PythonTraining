class Example:
    def __init__(self):
        self.public_var = "I am Public"         # Public attribute
        self._protected_var = "I am Protected"  # Protected attribute
        self.__private_var = "I am Private"     # Private attribute

    def public_method(self):
        return "Public method can be accessed anywhere"

    def _protected_method(self):
        return "Protected method can be accessed within subclass or instance (not enforced)"

    def __private_method(self):
        return "Private method, not directly accessible outside the class"

    def access_private(self):
        return self.__private_method()  # Private method accessed within class


# Creating object
obj = Example()

# Public attributes/methods can be accessed freely
print(obj.public_var)
print(obj.public_method())

# Protected attributes/methods can be accessed but should be used cautiously
print(obj._protected_var)
print(obj._protected_method())

# Private attributes/methods cannot be accessed directly
# print(obj.__private_var)  # Raises AttributeError
# print(obj.__private_method())  # Raises AttributeError

# Accessing private variables using name mangling
print(obj._Example__private_var)  # Works, but not recommended
print(obj.access_private())  # Accessing private method via a public method



class Parent:
    def __init__(self):
        self._protected_var = "Protected variable in Parent"

    def _protected_method(self):
        return "This is a protected method in Parent"


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_var = "Child variable"

    def use_protected(self):
        # Accessing the protected method from Parent within the Child class
        parent_msg = self._protected_method()
        return f"Child accessing: {parent_msg}"


# Creating an instance of Child
child_instance = Child()

# Accessing the protected method via a public method in Child
print(child_instance.use_protected())

# Note: Although you can technically call the protected method directly,
# it is discouraged to do so outside the class hierarchy.
print(child_instance._protected_method())


# Single Inheritance:
class Parent:
    def greet(self):
        return "Hello from Parent!"

class Child(Parent):
    pass

child = Child()
print(child.greet())  # Output: Hello from Parent!
