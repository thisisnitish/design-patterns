// STRATEGY DESIGN PATTERN CODE EXAMPLE

package main

import (
	"fmt"
	"slices"
)

// Strategy interface
type Strategy interface {
	Execute(data []int) []int
}

// Context
type Context struct {
	strategy Strategy
}

// Initiate the strategy
func InitiateStrategy(strategy Strategy) *Context {
	return &Context{strategy: strategy}
}

// Set the strategy at the run time
func (ctx *Context) SetStrategy(strategy Strategy) {
	ctx.strategy = strategy
}

// Execute the strategy at the run time
func (ctx *Context) ExecuteStrategy(data []int) []int {
	return ctx.strategy.Execute(data)
}

// Concrete Strategies
type AscendingStrategy struct{}

func (asc *AscendingStrategy) Execute(data []int) []int {
	slices.Sort(data)
	return data
}

type DescendingStrategy struct{}

func (desc *DescendingStrategy) Execute(data []int) []int {
	slices.Sort(data)
	slices.Reverse(data)
	return data
}

type DefaultStrategy struct{}

func (def *DefaultStrategy) Execute(data []int) []int {
	return data
}

func StrategyPattern() {
	data := []int{5, 1, 9, 2, 0}
	appA := InitiateStrategy(&AscendingStrategy{})
	resA := appA.ExecuteStrategy(data)
	fmt.Println("Ascending Strategy: ", resA) // Ascending Strategy:  [0 1 2 5 9]

	appA.SetStrategy(&DescendingStrategy{}) // set descending strategy and execute it
	resB := appA.ExecuteStrategy(data)
	fmt.Println("Descending Strategy: ", resB) // Descending Strategy:  [9 5 2 1 0]

	appA.SetStrategy(&DefaultStrategy{}) // set default strategy and execute it
	resC := appA.ExecuteStrategy(data)
	fmt.Println("Default Strategy: ", resC) // Default Strategy:  [9 5 2 1 0]
}

func main() {
	StrategyPattern()
}
