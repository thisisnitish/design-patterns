# PROXY DESIGN PATTERN CODE EXAMPLE

from abc import ABC, abstractmethod

# Inteface
class Subject(ABC):
    """
    The Subject interface declares common operations for both RealSubject and
    the Proxy. As long as the client works with RealSubject using this
    interface, you'll be able to pass it a proxy instead of a real subject.
    """

    @abstractmethod
    def request(self):
        pass


# RealSubject uses Subject Interface
class RealSubject(Subject):

    """
    The RealSubject contains some business logic and used to perform some useful work.
    """
    
    def request(self):
        print("RealSubject: Handling request.") 


# Poxy also uses Subject Interface
class Proxy(Subject):
    """
    The Proxy has an interface identical to the RealSubject.
    """

    def __init__(self, real_subject: RealSubject):
        self.real_subject = real_subject

    def request(self):
        if self.check_access():
            self.real_subject.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.", end="")


# Client Code
def client_code(subject: Subject):
    """
    The client code is supposed to work with all objects (both subjects and
    proxies) via the Subject interface in order to support both real subjects
    and proxies. In real life, however, clients mostly work with their real
    subjects directly. In this case, to implement the pattern more easily, you
    can extend your proxy from the real subject's class.
    """
    subject.request()


if __name__ == "__main__":
    print("Executing the client code with real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("\n")

    print("Executing the same client code with proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)