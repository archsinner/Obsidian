## The match operator
[[Pattern matching]]

We have used the `=` operator a couple times to assign variables in Elixir:

```
iex> x = 1
1
iex> x
1
```

In Elixir, the `=` operator is actually called _the match operator_. Let’s see why:

```
iex> x = 1
1
iex> 1 = x
1
iex> 2 = x
** (MatchError) no match of right hand side value: 1
```

Notice that `1 = x` is a valid expression, and it matched because both the left and right side are equal to 1. When the sides do not match, a `MatchError` is raised.

A variable can only be assigned on the left side of `=`:

```
iex> 1 = unknown
** (CompileError) iex:1: undefined function unknown/0
```

Since there is no variable `unknown` previously defined, Elixir assumed you were trying to call a function named `unknown/0`, but such a function does not exist.

