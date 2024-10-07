// OBSERVER DESIGN PATTERN CODE EXAMPLE

package main

import "fmt"

// Observer Interface
type Observer interface {
	Update(temperature int)
}

// Subject or Observable Interface
type Subject interface {
	Register(observer Observer)
	UnRegister(observer Observer)
	Notify()
}

// Concrete Subject or Observable
type WeatherStation struct {
	observers   []Observer
	temperature int
}

func (ws *WeatherStation) Register(observer Observer) {
	fmt.Println("Subject: Register an observer.")
	found, _ := checkElementExists(ws.observers, observer)

	if !found {
		ws.observers = append(ws.observers, observer)
	}
}

func (ws *WeatherStation) UnRegister(observer Observer) {
	fmt.Println("Subject: Unregister an observer.")
	found, idx := checkElementExists(ws.observers, observer)

	if found {
		ws.observers = append(ws.observers[:idx], ws.observers[idx+1:]...)
	}
}

func checkElementExists(observers []Observer, observer Observer) (bool, int) {
	found := false
	i := 0
	for ; i < len(observers); i++ {
		if observers[i] == observer {
			found = true
			break
		}
	}

	return found, i
}

func (ws *WeatherStation) Notify() {
	fmt.Println("Notifying observers....")
	for _, observer := range ws.observers {
		observer.Update(ws.GetTemperature())
	}
}

func (ws *WeatherStation) SetTemperature(temperature int) {
	ws.temperature = temperature
	ws.Notify()
}

func (ws *WeatherStation) GetTemperature() int {
	return ws.temperature
}

// Concrete Observers
type PhoneDisplay struct {
	station WeatherStation
}

func InitiatePhoneDisplay(station WeatherStation) *PhoneDisplay {
	phoneDisplay := &PhoneDisplay{
		station: station,
	}

	return phoneDisplay
}

func (pd *PhoneDisplay) Update(temperature int) {
	// temperature := pd.station.GetTemperature()
	fmt.Println("Phone Display updated with", temperature, "degrees Celsius")
}

func main() {
	weatherStation := &WeatherStation{}
	phoneDisplay := InitiatePhoneDisplay(*weatherStation)

	weatherStation.Register(phoneDisplay)
	weatherStation.SetTemperature(25)
}

// OUTPUT
/*
Subject: Register an observer.
Notifying observers....
Phone Display updated with 25 degrees Celsius
*/
