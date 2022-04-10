## if and unless
[[case, cond, and if]]

Besides `case` and `cond`, Elixir also provides `if/2` and `unless/2`, which are useful when you need to check for only one condition:

```
iex> if true do
...>   "This works!"
...> end
"This works!"
iex> unless true do
...>   "This will never be seen"
...> end
nil
```

If the condition given to `if/2` returns `false` or `nil`, the body given between `do`-`end` is not executed and instead it returns `nil`. The opposite happens with `unless/2`.

They also support `else` blocks:

```
iex> if nil do
...>   "This won't be seen"
...> else
...>   "This will"
...> end
"This will"
```

This is also a good opportunity to talk about variable scoping in Elixir. If any variable is declared or changed inside `if`, `case`, and similar constructs, the declaration and change will only be visible inside the construct. For example:

```
iex> x = 1
1
iex> if true do
...>   x = x + 1
...> end
2
iex> x
1
```

In said cases, if you want to change a value, you must return the value from the `if`:

```
iex> x = 1
1
iex> x = if true do
...>   x + 1
...> else
...>   x
...> end
2
```

> Note: An interesting note regarding `if/2` and `unless/2` is that they are implemented as macros in the language; they aren’t special language constructs as they would be in many languages. You can check the documentation and the source of `if/2` in [the `Kernel` module docs](https://hexdocs.pm/elixir/Kernel.html). The `Kernel` module is also where operators like `+/2` and functions like `is_function/2` are defined, all automatically imported and available in your code by default.

We have concluded the introduction to the most fundamental control-flow constructs in Elixir. Now it is time to talk about “Binaries, strings, and char lists”.