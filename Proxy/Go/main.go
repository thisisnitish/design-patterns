// PROXY DESIGN PATTERN CODE EXAMPLE

package main

import "fmt"

// Inteface
type Subject interface {
	Request()
}

// RealSubject uses Subject Interface
type RealSubject struct{}

func (r *RealSubject) Request() {
	fmt.Println("RealSubject: Handling Request")
}

// Poxy also uses Subject Interface
type Proxy struct {
	realSubject *RealSubject
}

func (p *Proxy) Request() {
	if p.CheckAccess() {
		p.realSubject.Request()
		p.LogAccess()
	}
}

func (p *Proxy) CheckAccess() bool {
	fmt.Printf("Checking access prior to firing a real request.\n")
	return true
}

func (p *Proxy) LogAccess() {
	fmt.Printf("Logging the time of the request.\n")
}

// Client Code
func ClientCode(subject Subject) {
	subject.Request()
}

func main() {
	fmt.Println("Executing the client code with real subject:")
	realSubject := &RealSubject{}
	ClientCode(realSubject)

	fmt.Println()

	fmt.Println("Executing the client code with proxy:")
	proxy := &Proxy{realSubject: realSubject}
	ClientCode(proxy)
}

/**
OUTPUT:
Executing the client code with real subject:
RealSubject: Handling Request

Executing the client code with proxy:
Checking access prior to firing a real request.
RealSubject: Handling Request
Logging the time of the request.
**/
