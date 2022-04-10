# Slices
[[Go]]
---

We already studied about the arrays in golang. But there is one drawback when using golang, they are of fixed size. If we want to increase the size, we need to create another array with higher capacity and copy over the values from the old array. Slices solve this problem.

## Slices

Slices are like arrays but they are dynamically resizable i.e. their size is not fixed similar to `list` in python. Slices are a layer of abstraction over arrays. So when on resizing, the underlying array is changed to a larger array and the contents are copied, but it is completely abstracted from the programmer.

The syntax for defining a slice is

```go
var <slice name> []<datatype of data stored in the slice>
```

This is an example of defining a slice.

```go
var exampleSlice []int
```

To add elements to a slice we use the `append()` function, as shown below

```go
exampleSlice = append(exampleSlice, 1)
exampleSlice = append(exampleSlice, 2)
exampleSlice = append(exampleSlice, 3)
```

We can do this in a single line like this

```go
exampleSlice := []int{1,2,3}
```

Remember we studied about the `:=` operator in go in the previous chapters. It enables us to skip adding the var keyword and the type.

To find the current length of the slice we use the `len()` function, and to find the capacity of the underlying array, we use the `cap()` function

```go
fmt.Printf("%d is the length of the Slice", len(exampleSlice))              // prints 3
fmt.Printf("%d is the capacity of the underlying array", cap(exampleSlice))
```

Now let's print the elements of the slice

```go
fmt.Println(exampleSlice)                   // prints [1 2 3]
```

You can also create a slice using the make function where you can also give an initial capacity to the slice.

```go
// here 0 is the initial length, and 5 is the initial capacity 
// i.e. we haven't added any values but the underlying array has a 
// initial capacity of 5 which is later changed dynamically to meet the requirement
exampleSlice := make([]int, 0, 5)

// You can skip the capacity and length and only give the type to get an empty slice
exampleSlice = make([]int)
```