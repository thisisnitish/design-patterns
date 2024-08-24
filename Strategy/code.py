# STRATEGY DESIGN PATTERN CODE EXAMPLE

from abc import ABC, abstractmethod
from typing import List

## Strategy interface
class Strategy(ABC):
    @abstractmethod
    def execute(self, data: List):
        pass



# Context Class
class Context:
    strategy: Strategy # strategy interface

    """
    Here, you can also create a constructor to set a strategy.
    Usually, the Context accepts a strategy through the constructor, 
    but also provides a setter to change it at runtime.
    """

    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def execute_strategy(self, data: List) -> List:
        return self.strategy.execute(data)


## Concrete strategies

"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""

class AscendingStrategy(Strategy):
    def execute(self, data: List) -> List:
        return sorted(data)
    

class DescendingStrategy(Strategy):
    def execute(self, data: List) -> List:
        return list(reversed(sorted(data)))


class DefaultStrategy(Strategy):
    def execute(self, data: List) -> List:
        return data
    

data = [5, 1, 9, 2, 0]

appA = Context(AscendingStrategy())
# appA.set_strategy(AscendingStrategy())
resA = appA.execute_strategy(data)
print("Ascending Strategy: ", resA)  # Ascending Strategy:  [0, 1, 2, 5, 9]

# appB = Context()
appA.set_strategy(DescendingStrategy())  ## set descending strategy and execute it
resB = appA.execute_strategy(data)
print("Descending Strategy: ", resB)  # Descending Strategy:  [9, 5, 2, 1, 0]

# appC = Context()
appA.set_strategy(DefaultStrategy()) ## set default strategy and execute it
resC = appA.execute_strategy(data)
print("Default Strategy:", resC)  # Default Strategy: [5, 1, 9, 2, 0]
