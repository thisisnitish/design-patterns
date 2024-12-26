# FACTORY DESIGN PATTERN CODE EXAMPLE - CREATIONAL DESIGN PATTERN

from abc import ABC, abstractmethod

# Interface for Pizza Class and it's processes
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

# Concrete Implementation for Pizza Class
class CheesePizza(Pizza):
    def prepare(self):
        print("Preparing Cheese Pizza")

    def bake(self):
        print("Baking Cheese Pizza")

    def cut(self):
        print("Cutting Cheese Pizza")

    def box(self):
        print("Boxing Cheese Pizza")

class VeggiePizza(Pizza):
    def prepare(self):
        print("Preparing Veggie Pizza")

    def bake(self):
        print("Baking Veggie Pizza")

    def cut(self):
        print("Cutting Veggie Pizza")

    def box(self):
        print("Boxing Veggie Pizza")

class HawaiianPizza(Pizza):
    def prepare(self):
        print("Preparing Hawaiian Pizza")

    def bake(self):
        print("Baking Hawaiian Pizza")

    def cut(self):
        print("Cutting Hawaiian Pizza")

    def box(self):
        print("Boxing Hawaiian Pizza")


# Interface for Factory Class
class PizzaFactory(ABC):
    @abstractmethod
    def createPizza(self, pizzaType):
        pass

# Concrete Implementation for Factory class
class NYPizzaFactory(PizzaFactory):

    def createPizza(self, pizzaType):
        if pizzaType == "Cheese":
            return CheesePizza()
        elif pizzaType == "Veggie":
            return VeggiePizza()
        elif pizzaType == "Hawaiian":
            return HawaiianPizza()
        else:
            return None
        
class ChicagoPizzaFactory(PizzaFactory):

    def createPizza(self, pizzaType):
        if pizzaType == "Cheese":
            return CheesePizza()
        elif pizzaType == "Veggie":
            return VeggiePizza()
        elif pizzaType == "Hawaiian":
            return HawaiianPizza()
        else:
            return None

# Creating Pizza Store  
class PizzaStore:
    pizzaFactory: PizzaFactory = None

    def __init__(self, pizzaFactory):
        self.pizzaFactory = pizzaFactory

    def orderPizza(self, pizzaType):
        pizza = self.pizzaFactory.createPizza(pizzaType)
        if pizza is not None:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.box()
        else:
            print("Invalid Pizza Type")
        

if __name__ == "__main__":
    nyPizzaFactory = NYPizzaFactory()
    chicagoPizzaFactory = ChicagoPizzaFactory()

    nyPizzaStore = PizzaStore(nyPizzaFactory)
    nyPizzaStore.orderPizza("Cheese")

    chicagoPizzaStore = PizzaStore(chicagoPizzaFactory)
    chicagoPizzaStore.orderPizza("Veggie")


# OUTPUT
"""
Preparing Cheese Pizza
Baking Cheese Pizza
Cutting Cheese Pizza
Boxing Cheese Pizza
Preparing Veggie Pizza
Baking Veggie Pizza
Cutting Veggie Pizza
Boxing Veggie Pizza
"""