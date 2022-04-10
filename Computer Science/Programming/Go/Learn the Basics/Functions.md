# Functions
[[Go]]
---

Functions provide a way to divide your code into logical blocks and reuse them minimising the time and effort and improve the managability of the code.

## Functions in Go

Functions in golang are defined using the `func` keyword.

The syntax to define a function in go

```go
func <name of the function> (<inputs to the function>) (<datatypes of return values from the function>) {
    // your code here
}
```

Let's write a add function using this syntax

```go
func add (a int, b int) int {
    return a + b
}
```

## How to call a function in your code

Calling a function is as easy as writing the function name and giving it the arguments. Now for an example let's call our add function in the main method.

```go
package main

import "fmt"

func main() {
    sum := add(3, 5)

    fmt.Println(sum)        // prints 8
}
```

Go also let's you ignore specific fields in the return values using the `_` variable.

```go
package main

import "fmt"

func sumAndDiff (a int, b int) (int, int) {
    return a + b, a - b
}

func main() {
    sum, _ := sumAndDiff(5, 3)      // the 2nd variable is ignored and not used

    fmt.Println(sum)                // prints 8
}
```

We can also add named return values so that we dont need to deliberately return something in the function. But beware, use this only in small functions.

```go
package main

import "fmt"

func add (a int, b int) (sum int) {         // here we are defining the variable name of what we are returning
    sum = a + b                             // so no need for a return statement, go takes care of it
}

func main() {
    sum := add(3, 5)

    fmt.Println(sum)                // prints 8
}
```