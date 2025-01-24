# SINGLE DESIGN PATTERN CODE EXAMPLE

# TODO: Implement Singleton Thread Safe Design Pattern in Python. Also, few other variations of it.

# NAIVE SINGLETON CODE EXAMPLE
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Any business logic which can be executed on its instance
        """
        pass


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

# OUTPUT
"""
Singleton works, both variables contain the same instance.
"""