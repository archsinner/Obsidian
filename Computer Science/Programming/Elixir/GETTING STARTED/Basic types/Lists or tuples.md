## Lists or tuples?
[[Basic types]]

What is the difference between lists and tuples?

Lists are stored in memory as linked lists, meaning that each element in a list holds its value and points to the following element until the end of the list is reached. This means accessing the length of a list is a linear operation: we need to traverse the whole list in order to figure out its size.

Similarly, the performance of list concatenation depends on the length of the left-hand list:

```
iex> list = [1, 2, 3]
[1, 2, 3]

# This is fast as we only need to traverse `[0]` to prepend to `list`
iex> [0] ++ list
[0, 1, 2, 3]

# This is slow as we need to traverse `list` to append 4
iex> list ++ [4]
[1, 2, 3, 4]
```

Tuples, on the other hand, are stored contiguously in memory. This means getting the tuple size or accessing an element by index is fast. However, updating or adding elements to tuples is expensive because it requires creating a new tuple in memory:

```
iex> tuple = {:a, :b, :c, :d}
{:a, :b, :c, :d}
iex> put_elem(tuple, 2, :e)
{:a, :b, :e, :d}
```

Note that this applies only to the tuple itself, not its contents. For instance, when you update a tuple, all entries are shared between the old and the new tuple, except for the entry that has been replaced. In other words, tuples and lists in Elixir are capable of sharing their contents. This reduces the amount of memory allocation the language needs to perform and is only possible thanks to the immutable semantics of the language.

Those performance characteristics dictate the usage of those data structures. One very common use case for tuples is to use them to return extra information from a function. For example, `File.read/1` is a function that can be used to read file contents. It returns a tuple:

```
iex> File.read("path/to/existing/file")
{:ok, "... contents ..."}
iex> File.read("path/to/unknown/file")
{:error, :enoent}
```

If the path given to `File.read/1` exists, it returns a tuple with the atom `:ok` as the first element and the file contents as the second. Otherwise, it returns a tuple with `:error` and the error description.

Most of the time, Elixir is going to guide you to do the right thing. For example, there is an `elem/2` function to access a tuple item but there is no built-in equivalent for lists:

```
iex> tuple = {:ok, "hello"}
{:ok, "hello"}
iex> elem(tuple, 1)
"hello"
```

When counting the elements in a data structure, Elixir also abides by a simple rule: the function is named `size` if the operation is in constant time (i.e. the value is pre-calculated) or `length` if the operation is linear (i.e. calculating the length gets slower as the input grows). As a mnemonic, both “length” and “linear” start with “l”.

For example, we have used 4 counting functions so far: `byte_size/1` (for the number of bytes in a string), `tuple_size/1` (for tuple size), `length/1` (for list length) and `String.length/1` (for the number of graphemes in a string). We use `byte_size` to get the number of bytes in a string – a cheap operation. Retrieving the number of Unicode graphemes, on the other hand, uses `String.length`, and may be expensive as it relies on a traversal of the entire string.

Elixir also provides `Port`, `Reference`, and `PID` as data types (usually used in process communication), and we will take a quick look at them when talking about processes. For now, let’s take a look at some of the basic operators that go with our basic types.