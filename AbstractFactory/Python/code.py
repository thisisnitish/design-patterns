# ABSTRACT FACTORY DESIGN PATTERN CODE EXAMPLE

from abc import ABC, abstractmethod

# Abstract Product Class or Interface
class Pizza(ABC):
    
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def cut(self):
        pass

    @abstractmethod
    def box(self):
        pass


# Concrete Product Classes
class NYCCheesePizza(Pizza):

    def prepare(self):
        print("Preparing NY Style Cheese Pizza")

    def bake(self):
        print("Baking NY Style Cheese Pizza")

    def cut(self):
        print("Cutting NY Style Cheese Pizza")

    def box(self):
        print("Boxing NY Style Cheese Pizza")

class NYCPepperoniPizza(Pizza):

    def prepare(self):
        print("Preparing NY Style Pepperoni Pizza")

    def bake(self):
        print("Baking NY Style Pepperoni Pizza")

    def cut(self):
        print("Cutting NY Style Pepperoni Pizza")

    def box(self):
        print("Boxing NY Style Pepperoni Pizza")

class ChicagoCheesePizza(Pizza):
    
    def prepare(self):
        print("Preparing Chicago Style Cheese Pizza")

    def bake(self):
        print("Baking Chicago Style Cheese Pizza")

    def cut(self):
        print("Cutting Chicago Style Cheese Pizza")

    def box(self):
        print("Boxing Chicago Style Cheese Pizza")

class ChicagoPepperoniPizza(Pizza):
    
    def prepare(self):
        print("Preparing Chicago Style Pepperoni Pizza")

    def bake(self):
        print("Baking Chicago Style Pepperoni Pizza")

    def cut(self):
        print("Cutting Chicago Style Pepperoni Pizza")

    def box(self):
        print("Boxing Chicago Style Pepperoni Pizza")

# Abstract Factory Class or Interface
class PizzaFactory(ABC):

    """
    In Abstract Factory class, different methods are defined for creating different types of products.
    """
    
    @abstractmethod
    def create_cheese_pizza(self) -> Pizza:
        pass

    @abstractmethod
    def create_pepperoni_pizza(self) -> Pizza:
        pass

# Concrete Factory Classes
class NYCPizzaFactory(PizzaFactory):
    
    def create_cheese_pizza(self) -> Pizza:
        return NYCCheesePizza()
    
    def create_pepperoni_pizza(self) -> Pizza:
        return NYCPepperoniPizza()
    
class ChicagoPizzaFactory(PizzaFactory):

    def create_cheese_pizza(self) -> Pizza:
        return ChicagoCheesePizza()
    
    def create_pepperoni_pizza(self) -> Pizza:
        return ChicagoPepperoniPizza()
    
# Client Code
def order_pizza(factory: PizzaFactory, pizzaType: str):
    pizza = None
    if pizzaType == "cheese":
        pizza = factory.create_cheese_pizza()
    elif pizzaType == "pepperoni":
        pizza = factory.create_pepperoni_pizza()
    else:
        print("Sorry, Invalid Pizza Type. Select another one.")
        return
    
    # Prepare, Bake, Cut, Box the Pizza
    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()


if __name__ == "__main__":
    # Creating the NYC Pizza Factory and ordering a Cheese Pizza
    nycPizzaFactory = NYCPizzaFactory()
    print("Ordering NY Style Cheese Pizza\n")
    order_pizza(nycPizzaFactory, "cheese")

    # Creating the Chicago Pizza Factory and ordering a Pepperoni Pizza
    chicagoPizzaFactory = ChicagoPizzaFactory()
    print("\nOrdering Chicago Style Pepperoni Pizza\n")
    order_pizza(chicagoPizzaFactory, "pepperoni")


# OUTPUT
"""
Ordering NY Style Cheese Pizza

Preparing NY Style Cheese Pizza
Baking NY Style Cheese Pizza
Cutting NY Style Cheese Pizza
Boxing NY Style Cheese Pizza

Ordering Chicago Style Pepperoni Pizza

Preparing Chicago Style Pepperoni Pizza
Baking Chicago Style Pepperoni Pizza
Cutting Chicago Style Pepperoni Pizza
Boxing Chicago Style Pepperoni Pizza
"""