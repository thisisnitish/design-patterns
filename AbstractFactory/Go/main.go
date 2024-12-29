// ABSTRACT FACTORY DESIGN PATTERN CODE EXAMPLE

package main

import "fmt"

// Abstract Product Class or Interface
type Pizza interface {
	Prepare()
	Bake()
	Cut()
	Box()
}

// Concrete Product Classes
type NYCCheesePizza struct{}

func (p *NYCCheesePizza) Prepare() {
	fmt.Println("Preparing NY Cheese Pizza")
}

func (p *NYCCheesePizza) Bake() {
	fmt.Println("Baking NY Cheese Pizza")
}

func (p *NYCCheesePizza) Cut() {
	fmt.Println("Cutting NY Cheese Pizza")
}

func (p *NYCCheesePizza) Box() {
	fmt.Println("Boxing NY Cheese Pizza")
}

type NYCPepperoniPizza struct{}

func (p *NYCPepperoniPizza) Prepare() {
	fmt.Println("Preparing NY Pepperoni Pizza")
}

func (p *NYCPepperoniPizza) Bake() {
	fmt.Println("Baking NY Pepperoni Pizza")
}

func (p *NYCPepperoniPizza) Cut() {
	fmt.Println("Cutting NY Pepperoni Pizza")
}

func (p *NYCPepperoniPizza) Box() {
	fmt.Println("Boxing NY Pepperoni Pizza")
}

type ChicagoCheesePizza struct{}

func (p *ChicagoCheesePizza) Prepare() {
	fmt.Println("Preparing Chicago Cheese Pizza")
}

func (p *ChicagoCheesePizza) Bake() {
	fmt.Println("Baking Chicago Cheese Pizza")
}

func (p *ChicagoCheesePizza) Cut() {
	fmt.Println("Cutting Chicago Cheese Pizza")
}

func (p *ChicagoCheesePizza) Box() {
	fmt.Println("Boxing Chicago Cheese Pizza")
}

type ChicagoPepperoniPizza struct{}

func (p *ChicagoPepperoniPizza) Prepare() {
	fmt.Println("Preparing Chicago Pepperoni Pizza")
}

func (p *ChicagoPepperoniPizza) Bake() {
	fmt.Println("Baking Chicago Pepperoni Pizza")
}

func (p *ChicagoPepperoniPizza) Cut() {
	fmt.Println("Cutting Chicago Pepperoni Pizza")
}

func (p *ChicagoPepperoniPizza) Box() {
	fmt.Println("Boxing Chicago Pepperoni Pizza")
}

// Abstract Factory Interface
type PizzaFactory interface {
	CreateCheesePizza() Pizza
	CreatePepperoniPizza() Pizza
}

// Concrete Factory Classes
type NYCPizzaFactory struct{}

func (f *NYCPizzaFactory) CreateCheesePizza() Pizza {
	return &NYCCheesePizza{}
}

func (f *NYCPizzaFactory) CreatePepperoniPizza() Pizza {
	return &NYCPepperoniPizza{}
}

type ChicagoPizzaFactory struct{}

func (f *ChicagoPizzaFactory) CreateCheesePizza() Pizza {
	return &ChicagoCheesePizza{}
}

func (f *ChicagoPizzaFactory) CreatePepperoniPizza() Pizza {
	return &ChicagoPepperoniPizza{}
}

// Client Code
func OrderPizza(factory PizzaFactory, pizzaType string) {
	var pizza Pizza

	switch pizzaType {
	case "cheese":
		pizza = factory.CreateCheesePizza()
	case "pepperoni":
		pizza = factory.CreatePepperoniPizza()
	default:
		fmt.Println("Sorry, Invalid Pizza Type. Select another one.")
	}

	// Prepare, Bake, Cut and Box the Pizza
	pizza.Prepare()
	pizza.Bake()
	pizza.Cut()
	pizza.Box()
}

func main() {
	// Creating the NYC Pizza Factory and ordering a Cheese Pizza
	nycPizzaFactory := &NYCPizzaFactory{}
	fmt.Println("Ordering NY Style Cheese Pizza")
	fmt.Println()
	OrderPizza(nycPizzaFactory, "cheese")

	fmt.Println()
	// Creating the Chicago Pizza Factory and ordering a Pepperoni Pizza
	chicagoPizzaFactory := &ChicagoPizzaFactory{}
	fmt.Println("Ordering Chicago Style Pepperoni Pizza")
	fmt.Println()
	OrderPizza(chicagoPizzaFactory, "pepperoni")
}

// OUTPUT

/*
Ordering NY Style Cheese Pizza

Preparing NY Cheese Pizza
Baking NY Cheese Pizza
Cutting NY Cheese Pizza
Boxing NY Cheese Pizza

Ordering Chicago Style Pepperoni Pizza

Preparing Chicago Pepperoni Pizza
Baking Chicago Pepperoni Pizza
Cutting Chicago Pepperoni Pizza
Boxing Chicago Pepperoni Pizza
*/
