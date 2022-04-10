# Variables
[[Go]]
---

A variable is a name given to a storage area that the programs can manipulate. The name of a variable can be composed of letters, digits, and the underscore character. It must begin with either a letter or an underscore.

The general code to declare a variable in golang is

```go
var <name of variable> <type of variable>
```

### Numbers

Variables are arithmetic types and represent the following values throughout the program. a) integer types b) floating point

To define an integer, use the following syntax:

```go
var a int = 4
var b, c int
b = 5
c = 10
fmt.Println(a)
fmt.Println(b + c)
```

To define a floating point number, use the following syntax:

```go
var d float64 = 9.14
fmt.Println(d)
```

### Strings

Strings in Go are defined with double quotes.

```go
var s string = "This is string s"
fmt.Println(s)
```

Single quotes are not used to enable the use of apostrophes in strings without having to escape.

```go
var s string = "Don't worry about apostrophes"
fmt.Println(s)
```

We can also define multiple line strings wrapping the string in `` quotes.

```go
var s string = `This is a string spanning multiple lines
This is the second line
And this is the third`

fmt.Println(s)
```

### Booleans

Golang supports boolean values with the keywords `true` and `false`

Boolean variables are declared in go as follows

```go
var b bool = true
```

### Shorthand Declaration

The `:=` notation serves both as a declaration and as initialization. `foo := "bar"` is equivalent to `var foo string = "bar"`

```go
a := 9
b := "golang"
c := 4.17
d := false
e := "Hello"
f := `Do you like golang, so far?`
g := 'M'
h := true

fmt.Println(a)
fmt.Println(b)
fmt.Println(c)
fmt.Println(d)
fmt.Println(e)
fmt.Println(f)
fmt.Println(g)
fmt.Println(h)
```