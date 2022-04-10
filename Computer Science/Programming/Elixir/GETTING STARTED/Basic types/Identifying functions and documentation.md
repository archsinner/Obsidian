## Identifying functions and documentation
[[Basic types]]
Functions in Elixir are identified by both their name and their arity. The arity of a function describes the number of arguments that the function takes. From this point on we will use both the function name and its arity to describe functions throughout the documentation. `trunc/1` identifies the function which is named `trunc` and takes `1` argument, whereas `trunc/2` identifies a different (nonexistent) function with the same name but with an arity of `2`.

We can also use this syntax to access documentation. The Elixir shell defines the `h` function, which you can use to access documentation for any function. For example, typing `h trunc/1` is going to print the documentation for the `trunc/1` function:

```
iex> h trunc/1
                             def trunc()

Returns the integer part of number.
```

`h trunc/1` works because it is defined in the `Kernel` module. All functions in the `Kernel` module are automatically imported into our namespace. Most often you will also include the module name when looking up for documentation for a given function:

```
iex> h Kernel.trunc/1
                             def trunc()

Returns the integer part of number.
```

You can use the module+function to lookup for anything, including operators (try `h Kernel.+/2`). Invoking `h` without arguments displays the documentation for `IEx.Helpers`, which is where `h` and other functionality is defined.