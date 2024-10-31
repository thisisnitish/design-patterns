// DECORATOR DESIGN PATTERN CODE EXAMPLE

package main

import "fmt"

// Beverage abstract method
type Beverage interface {
	GetDescription() string
	Cost() float64
}

// Add-on abstract method (Condiments given in the book), Aka Decorators
type AddOn struct {
	beverage Beverage
}

func (addOn *AddOn) Cost() float64 {
	return 0.0
}

func (addOn *AddOn) GetDescription() string {
	return ""
}

// Concrete Beverage

type Espresso struct{}

func (espresso *Espresso) GetDescription() string {
	return "Espresso Beverage"
}

func (espresso *Espresso) Cost() float64 {
	return 1.5
}

type HouseBlend struct{}

func (houseBlend *HouseBlend) GetDescription() string {
	return "House Blend Beverage"
}

func (houseBlend *HouseBlend) Cost() float64 {
	return 2.0
}

type DarkRoast struct{}

func (darkRoast *DarkRoast) GetDescription() string {
	return "Dark Roast Beverage"
}

func (darkRoast *DarkRoast) Cost() float64 {
	return 3.5
}

// Concrete AddOns

type Caramel struct {
	AddOn
}

func (caramel *Caramel) GetDescription() string {
	return caramel.beverage.GetDescription() + " with Caramel"
}

func (caramel *Caramel) Cost() float64 {
	return caramel.beverage.Cost() + 3.5
}

type Soy struct {
	AddOn
}

func (soy *Soy) GetDescription() string {
	return soy.beverage.GetDescription() + " with Soy"
}

func (soy *Soy) Cost() float64 {
	return soy.beverage.Cost() + 2.7
}

type Whip struct {
	AddOn
}

func (whip *Whip) GetDescription() string {
	return whip.beverage.GetDescription() + " with Whip"
}

func (whip *Whip) Cost() float64 {
	return whip.beverage.Cost() + 2.5
}

func main() {
	espresso := &Espresso{}
	darkRoast := &DarkRoast{}
	houseBlend := &HouseBlend{}

	fmt.Println(espresso.GetDescription(), "costs $", espresso.Cost())
	fmt.Println(darkRoast.GetDescription(), "costs $", darkRoast.Cost())
	fmt.Println(houseBlend.GetDescription(), "costs $", houseBlend.Cost())

	// Only one AddOn here for each beverage
	caramelWithEspresso := &Caramel{AddOn{espresso}}
	fmt.Println(caramelWithEspresso.GetDescription(), "costs $", caramelWithEspresso.Cost())

	soyWithEspresso := &Soy{AddOn{espresso}}
	fmt.Println(soyWithEspresso.GetDescription(), "costs $", soyWithEspresso.Cost())

	soyWithDarkRoast := &Soy{AddOn{darkRoast}}
	fmt.Println(soyWithDarkRoast.GetDescription(), "costs $", soyWithDarkRoast.Cost())

	whipWithDarkRoast := &Whip{AddOn{darkRoast}}
	fmt.Println(whipWithDarkRoast.GetDescription(), "costs $", whipWithDarkRoast.Cost())

	// Multiple AddOn for each beverage
	caramelSoyEspresso := &Caramel{AddOn{&Soy{AddOn{espresso}}}}
	fmt.Println(caramelSoyEspresso.GetDescription(), "costs $", caramelSoyEspresso.Cost())

	whipSoyHouseBlend := &Whip{AddOn{&Soy{AddOn{houseBlend}}}}
	fmt.Println(whipSoyHouseBlend.GetDescription(), "costs $", whipSoyHouseBlend.Cost())
}

// OUTPUT
/*
Espresso Beverage costs $ 1.5
Dark Roast Beverage costs $ 3.5
House Blend Beverage costs $ 2
Espresso Beverage with Caramel costs $ 5
Espresso Beverage with Soy costs $ 4.2
Dark Roast Beverage with Soy costs $ 6.2
Dark Roast Beverage with Whip costs $ 6
Espresso Beverage with Soy with Caramel costs $ 7.7
House Blend Beverage with Soy with Whip costs $ 7.2
*/
