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
    Here, you can also create a constructor to set a strategy
    """

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

appA = Context()
appA.set_strategy(AscendingStrategy())
resA = appA.execute_strategy(data)
print("Ascending Strategy: ", resA)

appB = Context()
appB.set_strategy(DescendingStrategy())
resB = appB.execute_strategy(data)
print("Descending Strategy: ", resB)

appC = Context()
appC.set_strategy(DefaultStrategy())
resC = appC.execute_strategy(data)
print("Default Strategy:", resC)
