## Basic arithmetic
[[Basic types]]
Open up `iex` and type the following expressions:

```
iex> 1 + 2
3
iex> 5 * 5
25
iex> 10 / 2
5.0
```

Notice that `10 / 2` returned a float `5.0` instead of an integer `5`. This is expected. In Elixir, the operator `/` always returns a float. If you want to do integer division or get the division remainder, you can invoke the `div` and `rem` functions:

```
iex> div(10, 2)
5
iex> div 10, 2
5
iex> rem 10, 3
1
```

Notice that Elixir allows you to drop the parentheses when invoking named functions with at least one argument. This feature gives a cleaner syntax when writing declarations and control-flow constructs. However, Elixir developers generally prefer to use parentheses.

Elixir also supports shortcut notations for entering binary, octal, and hexadecimal numbers:

```
iex> 0b1010
10
iex> 0o777
511
iex> 0x1F
31
```

Float numbers require a dot followed by at least one digit and also support `e` for scientific notation:

```
iex> 1.0
1.0
iex> 1.0e-10
1.0e-10
```

Floats in Elixir are 64-bit double precision.

You can invoke the `round` function to get the closest integer to a given float, or the `trunc` function to get the integer part of a float.

```
iex> round(3.58)
4
iex> trunc(3.58)
3
```