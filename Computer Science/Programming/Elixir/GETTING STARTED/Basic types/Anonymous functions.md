## Anonymous functions
[[Basic types]]

Elixir also provides anonymous functions. Anonymous functions allow us to store and pass executable code around as if it was an integer or a string. They are delimited by the keywords `fn` and `end`:

```
iex> add = fn a, b -> a + b end
[[Function]]<12.71889879/2 in :erl_eval.expr/5>
iex> add.(1, 2)
3
iex> is_function(add)
true
```

In the example above, we defined an anonymous function that receives two arguments, `a` and `b`, and returns the result of `a + b`. The arguments are always on the left-hand side of `->` and the code to be executed on the right-hand side. The anonymous function is stored in the variable `add`.

We can invoke anonymous functions by passing arguments to it. Note that a dot (`.`) between the variable and parentheses is required to invoke an anonymous function. The dot ensures there is no ambiguity between calling the anonymous function matched to a variable `add` and a named function `add/2`. We will write our own named functions when dealing with [Modules and Functions](https://elixir-lang.org/getting-started/modules-and-functions.html). For now, just remember that Elixir makes a clear distinction between anonymous functions and named functions.

Anonymous functions in Elixir are also identified by the number of arguments they receive. We can check if a function is of any given arity by using `is_function/2`:

```
# check if add is a function that expects exactly 2 arguments
iex> is_function(add, 2)
true
# check if add is a function that expects exactly 1 argument
iex> is_function(add, 1)
false
```

Finally, anonymous functions can also access variables that are in scope when the function is defined. This is typically referred to as closures, as they close over their scope. Let’s define a new anonymous function that uses the `add` anonymous function we have previously defined:

```
iex> double = fn a -> add.(a, a) end
[[Function]]<6.71889879/1 in :erl_eval.expr/5>
iex> double.(2)
4
```

A variable assigned inside a function does not affect its surrounding environment:

```
iex> x = 42
42
iex> (fn -> x = 0 end).()
0
iex> x
42
```