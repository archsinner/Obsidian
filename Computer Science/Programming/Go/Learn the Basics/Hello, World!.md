# Hello, World!
[[Go]]
---

Welcome to the first tutorial. This tutorial will guide you through your first go program.

Golang is a modern statistically typed and compiled language from Google.

In each golang program you need to define a package name at the top. So if you need to import your code into some other program you can use this package name to import. Execution of a golang project starts in the package `"main"`. So let's define our package as main.

```go
package main
```

Go follows a similar pattern as C and has a main function where the execution begins. In go functions are defined using `func` keyword.

This is an example main function

```go
func main () {

}
```

Now to print something we need to use the Println function from the package `"fmt"`

To import a function you just write import following the package name in "".

```go
import "somemodule"
```

Here is an example program to print "Hello World!"

```go
package main

import "fmt"

func main () {
    fmt.Println("This line is printed")
}
```

We dont need to add semi colons after each line in Go. The compiler takes care of it.

The `fmt` package also has a `Printf()` function similar to printf in C. It can be used in the same way as it is used in C.

```go
fmt.Printf("%d is a number",10)
```