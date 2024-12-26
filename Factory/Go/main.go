// FACTORY DESIGN PATTERN CODE EXAMPLE - CREATIONAL DESIGN PATTERN

package main

import "fmt"

// Interface for Pizza Class and it's processes
type Pizza interface {
	Prepare()
	Bake()
	Cut()
	Box()
}

// Concrete Implementation for Pizza Class
type CheesePizza struct{}

func (cp *CheesePizza) Prepare() {
	fmt.Println("Preparing Cheese Pizza")
}

func (cp *CheesePizza) Bake() {
	fmt.Println("Baking Cheese Pizza")
}

func (cp *CheesePizza) Cut() {
	fmt.Println("Cutting Cheese Pizza")
}

func (cp *CheesePizza) Box() {
	fmt.Println("Boxing Cheese Pizza")
}

type VeggiePizza struct{}

func (vp *VeggiePizza) Prepare() {
	fmt.Println("Preparing Veggie Pizza")
}

func (vp *VeggiePizza) Bake() {
	fmt.Println("Baking Veggie Pizza")
}

func (vp *VeggiePizza) Cut() {
	fmt.Println("Cutting Veggie Pizza")
}

func (vp *VeggiePizza) Box() {
	fmt.Println("Boxing Veggie Pizza")
}

type HawaiianPizza struct{}

func (hp *HawaiianPizza) Prepare() {
	fmt.Println("Preparing Hawaiian Pizza")
}

func (hp *HawaiianPizza) Bake() {
	fmt.Println("Baking Hawaiian Pizza")
}

func (hp *HawaiianPizza) Cut() {
	fmt.Println("Cutting Hawaiian Pizza")
}

func (hp *HawaiianPizza) Box() {
	fmt.Println("Boxing Hawaiian Pizza")
}

// Interface for Factory Class
type PizzaFactory interface {
	CreatePizza(pizzaType string) Pizza
}

// Concrete Implementation for Factory Class
type NYPizzaFactory struct{}

func (nyf *NYPizzaFactory) CreatePizza(pizzaType string) Pizza {
	switch pizzaType {
	case "cheese":
		return &CheesePizza{}
	case "veggie":
		return &VeggiePizza{}
	case "hawaiian":
		return &HawaiianPizza{}
	default:
		return nil
	}
}

type ChicagoPizzaFactory struct{}

func (cpf *ChicagoPizzaFactory) CreatePizza(pizzaType string) Pizza {
	switch pizzaType {
	case "cheese":
		return &CheesePizza{}
	case "veggie":
		return &VeggiePizza{}
	case "hawaiian":
		return &HawaiianPizza{}
	default:
		return nil
	}
}

// Creating Pizza Store
type PizzaStore struct {
	pizzaFactory PizzaFactory
}

func (ps *PizzaStore) OrderPizza(pizzaType string) Pizza {
	pizza := ps.pizzaFactory.CreatePizza(pizzaType)

	if pizza != nil {
		pizza.Prepare()
		pizza.Bake()
		pizza.Cut()
		pizza.Box()
	} else {
		fmt.Println("Invalid pizza type.")
		return nil
	}

	return pizza
}

func main() {
	nyPizzaFactory := &NYPizzaFactory{}
	chicagoPizzaFactory := &ChicagoPizzaFactory{}

	nyPizzaStore := &PizzaStore{nyPizzaFactory}
	chicagoPizzaStore := &PizzaStore{chicagoPizzaFactory}

	nyPizzaStore.OrderPizza("cheese")
	chicagoPizzaStore.OrderPizza("veggie")
}

// Output
/*
Preparing Cheese Pizza
Baking Cheese Pizza
Cutting Cheese Pizza
Boxing Cheese Pizza
Preparing Veggie Pizza
Baking Veggie Pizza
Cutting Veggie Pizza
Boxing Veggie Pizza
*/
