# Arrays
[[Go]]
---

## Arrays

Arrays are essentially storage spaces that can be filled with as much data as one would like. Variables, unlike arrays, can only contain one piece of data. Now there are some caveats. For instance, an array is syntactically created using one data type, just like variables. Yet, an array grants ease of access and far more capabilities when considering large/vast amounts of data compared to a variable(single storage space/value).

A array in golang has fixed size similar to C and C++ that we give while we define it. We can't change the size of the array dynamically while the program is running.

## Examples

Arrays in golang are defined using the syntax,

```go
var <name of array> [<size of array>]<type of data stored in the array>
```

Arrays in golang are 0 indexed i.e. the index starts from 0. Let's make some arrays using the syntax given above

```go
// An array named favNums filled with 3 integers
var favNums [3]int

// Insert data into the array
// The first storage space will be assigned the value of 1. It has an index of 0.
favNums[0] = 1
// The second storage space will be assigned the value of 2. It has an index of 1.
favNums[1] = 2
// The third and final storage space will be assigned the value of 3. It has an index of 2.
favNums[2] = 3
```

An alternative syntax to the creation of arrays in golang is:

```go
favNums := [4] int {50, 25, 30, 33}
```

In order to access members of an array, reference the storage space's address or number you used to create it.

```go
fmt.Println(favNums[0])
```

output:

```go
50
```