# CHAIN OF RESPONSIBILITY DESIGN PATTERN CODE EXAMPLE

"""
This design pattern is very important. Application usage for this are:
1. Design ATM.
2. Design Vending Maching of any type.
3. Design Logger.
"""


from abc import ABC, abstractmethod

# Handler Interface
class Handler(ABC):

    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

        return handler

    @abstractmethod
    def handle(self, request: str):
        if self.next_handler:
            return self.next_handler.handle(request)
        
        return None  # If you don't return then also it will work


# Concrete Handlers
class ConcreteHandlerA(Handler):
    def handle(self, request: str):
        if request == "A":
            return "Request A is processed"
        else:
            return super().handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request: str):
        if request == "B":
            return "Request B is processed"
        else:
            return super().handle(request)


class ConcreteHandlerC(Handler):
    def handle(self, request: str):
        if request == "C":
            return "Request C is processed"
        else:
            return super().handle(request)


def client_code(handler: Handler):
    for request in ["A", "B", "C", "D"]:
        result = handler.handle(request)
        if result:
            print(result)
        else:
            print(f"Request {request} didn't processed at all")


if __name__ == "__main__":
    a = ConcreteHandlerA()
    b = ConcreteHandlerB()
    c = ConcreteHandlerC()

    a.set_next(b).set_next(c)

    client_code(a)