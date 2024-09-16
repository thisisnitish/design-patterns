# OBSERVER DESIGN PATTERN CODE EXAMPLE

"""
The general gist is:
1. You have a Subject and a Observer. Subject is also k/a Observables.
2. Observers are interested in anything say a state changes in a Subject.
3. If the state of the Subject changes, then it notifies the observer.
4. After that, Observer react to it or say perform some further actions.
"""

from abc import ABC, abstractmethod
from typing import List

# Observer Interface
class Observer(ABC):
    """
    Observer interface has a update method
    """
    @abstractmethod
    def update(self) -> None:
        pass

# Subject or Observable Interface
class Subject(ABC):
    """
    Subject interface has a set of methods
    """
    @abstractmethod
    def register(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def unregister(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass



# Concrete Subject or Observable
class WeatherStation(Subject):
    observers: List[Observer] = []
    temperature: int = None

    def register(self, observer: Observer) -> None:
        print("Subject: Register an observer.")
        if observer not in self.observers:
            self.observers.append(observer)

    def unregister(self, observer: Observer) -> None:
        print("Subject: Unregister an observer.")
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self) -> None:
        print("Notifying observers....")
        for observer in self.observers:
            observer.update()

    def set_temperature(self, temperature: int) -> None:
        """
        This is some kind of business logic you can say. Think of it as a
        state. If state changes, we notify the observer.
        """
        self.temperature = temperature
        self.notify()

    def get_temperature(self) -> int:
        return self.temperature


# Concrete Observers
class PhoneDisplay(Observer):
    station: WeatherStation = None

    def __init__(self, station: WeatherStation) -> None:
        self.station = station

    def update(self) -> int:
       temperature = self.station.get_temperature()
       print(f"Phone Display updated with {temperature} degrees Celsius")


weather_station = WeatherStation()
phone_display = PhoneDisplay(weather_station)

weather_station.register(phone_display)
weather_station.set_temperature(25)

# OUTPUT
"""
Subject: Register an observer.
Notifying observers....
Phone Display updated with 25 degrees Celsius
"""