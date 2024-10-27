# DECORATOR DESIGN PATTERN CODE EXAMPLE

from abc import ABC, abstractmethod

# Beverage abstract method
class Beverage(ABC):

    """
    The Beverage is an abstract class contains get_description and 
    cost methods which can be altered by other concrete beverages 
    and addons or decorators or condiments
    """

    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def cost(self):
        pass


# Add-on abstract method (Condiments given in the book), Aka Decorators
class AddOn(Beverage, ABC):

    """
    AddOn is an abstract of Beverage type. In short, AddOn is a Beverage 
    and has a Beverage. The primary purpose of this class is to define the 
    wrapping interface for all concrete decorators.
    """

    beverage: Beverage = None  # AddOn has-a beverage

    def __init__(self, beverage) -> None:
        self.beverage = beverage

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass


# Concrete Beverage

"""
Concrete Beverage implements its own get_description and cost method
"""

class Espresso(Beverage):
    def get_description(self):
        return "Espresso Beverage"
    
    def cost(self):
        return 1.5


class HouseBlend(Beverage):
    def get_description(self):
        return "House Blend Beverage"
    
    def cost(self):
        return 2.0
    
class DarkRoast(Beverage):
    def get_description(self):
        return "Dark Roast Beverage"
    
    def cost(self):
        return 3.5


# Concrete AddOns

"""
Concrete AddOns implements their own get_description, cost method but it also
takes the cost of the beverage and do some calculations to it, say (Addition).
"""

class Caramel(AddOn):
    def get_description(self):
        return self.beverage.get_description() + " with Caramel"
    
    def cost(self):
        return self.beverage.cost() + 3.5
    

class Soy(AddOn):
    def get_description(self):
        return self.beverage.get_description() + " with Soy"
    
    def cost(self):
        return self.beverage.cost() + 2.7
    

class Whip(AddOn):
    def get_description(self):
        return self.beverage.get_description() + " with Whip"
    
    def cost(self):
        return self.beverage.cost() + 2.5
    


if __name__ == "__main__":

    espresso = Espresso()
    dark_roast = DarkRoast()
    house_blend = HouseBlend()
    print(espresso.get_description(), 'costs $', espresso.cost())
    print(dark_roast.get_description(), 'costs $', dark_roast.cost())
    print(house_blend.get_description(), 'costs $', house_blend.cost())

    # Only one AddOn here for each beverage
    caramel_with_espresso = Caramel(espresso)
    print(caramel_with_espresso.get_description(), 'costs $', caramel_with_espresso.cost())

    soy_with_espresso = Soy(espresso)
    print(soy_with_espresso.get_description(), 'costs $', soy_with_espresso.cost())

    soy_with_dark_roast = Soy(dark_roast)
    print(soy_with_dark_roast.get_description(), 'costs $', soy_with_dark_roast.cost())

    whip_with_dark_roast = Whip(dark_roast)
    print(whip_with_dark_roast.get_description(), 'costs $', whip_with_dark_roast.cost())

    # Multiple AddOn for each beverage
    caramel_soy_espresso = Caramel(Soy(espresso))
    print(caramel_soy_espresso.get_description(), 'costs $', caramel_soy_espresso.cost())

    whip_soy_house_blend = Whip(Soy(house_blend))
    print(whip_soy_house_blend.get_description(), 'costs $', whip_soy_house_blend.cost())    

    

# OUTPUT
"""
Espresso Beverage costs $ 1.5
Dark Roast Beverage costs $ 3.5
House Blend Beverage costs $ 2.0
Espresso Beverage with Caramel costs $ 5.0
Espresso Beverage with Soy costs $ 4.2
Dark Roast Beverage with Soy costs $ 6.2
Dark Roast Beverage with Whip costs $ 6.0
Espresso Beverage with Soy with Caramel costs $ 7.7
House Blend Beverage with Soy with Whip costs $ 7.2
"""