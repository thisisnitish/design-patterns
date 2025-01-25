// CHAIN OF RESPONSIBILITY DESIGN PATTERN CODE EXAMPLE

package main

// Handler Interface
type Handler interface {
	SetNext(handler Handler) Handler
	Handle(request string) string
}

// Concrete Handlers
type ConcreteHandlerA struct {
	next Handler
}

func (aHandler *ConcreteHandlerA) SetNext(handler Handler) Handler {
	aHandler.next = handler
	return handler
}

func (aHandler *ConcreteHandlerA) Handle(request string) string {
	if request == "A" {
		return "Request A is processed"
	} else if aHandler.next != nil {
		return aHandler.next.Handle(request)
	} else {
		return ""
	}

}

type ConcreteHandlerB struct {
	next Handler
}

func (bHandler *ConcreteHandlerB) SetNext(handler Handler) Handler {
	bHandler.next = handler
	return handler
}

func (bHandler *ConcreteHandlerB) Handle(request string) string {
	if request == "B" {
		return "Request B is processed"
	} else if bHandler.next != nil {
		return bHandler.next.Handle(request)
	} else {
		return ""
	}
}

type ConcreteHandlerC struct {
	next Handler
}

func (cHandler *ConcreteHandlerC) SetNext(handler Handler) Handler {
	cHandler.next = handler
	return handler
}

func (cHandler *ConcreteHandlerC) Handle(request string) string {
	if request == "C" {
		return "Request C is processed"
	} else if cHandler.next != nil {
		return cHandler.next.Handle(request)
	} else {
		return ""
	}
}

func ClientCode(handler Handler) {
	requests := []string{"A", "B", "C", "D"}

	for _, request := range requests {
		result := handler.Handle(request)
		if result != "" {
			println(result)
		} else {
			println("Request", request, "didn't processed at all")
		}
	}

}

func main() {
	a := &ConcreteHandlerA{}
	b := &ConcreteHandlerB{}
	c := &ConcreteHandlerC{}

	a.SetNext(b).SetNext(c)

	ClientCode(a)

}

// OUTPUT
/*
Request A is processed
Request B is processed
Request C is processed
Request D didn't processed at all
*/
