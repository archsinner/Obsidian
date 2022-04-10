## Booleans
[[Basic types]]

Elixir supports `true` and `false` as booleans:

```
iex> true
true
iex> true == false
false
```

Elixir provides a bunch of predicate functions to check for a value type. For example, the `is_boolean/1` function can be used to check if a value is a boolean or not:

```
iex> is_boolean(true)
true
iex> is_boolean(1)
false
```

You can also use `is_integer/1`, `is_float/1` or `is_number/1` to check, respectively, if an argument is an integer, a float, or either.