## The pin operator
[[Pattern matching]]

Variables in Elixir can be rebound:

```
iex> x = 1
1
iex> x = 2
2
```

However, there are times when we don’t want variables to be rebound.

Use the pin operator `^` when you want to pattern match against a variable’s _existing value_ rather than rebinding the variable.

```
iex> x = 1
1
iex> ^x = 2
** (MatchError) no match of right hand side value: 2
```

Because we have pinned `x` when it was bound to the value of `1`, it is equivalent to the following:

```
iex> 1 = 2
** (MatchError) no match of right hand side value: 2
```

Notice that we even see the exact same error message.

We can use the pin operator inside other pattern matches, such as tuples or lists:

```
iex> x = 1
1
iex> [^x, 2, 3] = [1, 2, 3]
[1, 2, 3]
iex> {y, ^x} = {2, 1}
{2, 1}
iex> y
2
iex> {y, ^x} = {2, 2}
** (MatchError) no match of right hand side value: {2, 2}
```

Because `x` was bound to the value of `1` when it was pinned, this last example could have been written as:

```
iex> {y, 1} = {2, 2}
** (MatchError) no match of right hand side value: {2, 2}
```

If a variable is mentioned more than once in a pattern, all references should bind to the same value:

```
iex> {x, x} = {1, 1}
{1, 1}
iex> {x, x} = {1, 2}
** (MatchError) no match of right hand side value: {1, 2}
```

In some cases, you don’t care about a particular value in a pattern. It is a common practice to bind those values to the underscore, `_`. For example, if only the head of the list matters to us, we can assign the tail to underscore:

```
iex> [head | _] = [1, 2, 3]
[1, 2, 3]
iex> head
1
```

The variable `_` is special in that it can never be read from. Trying to read from it gives a compile error:

```
iex> _
** (CompileError) iex:1: invalid use of _. "_" represents a value to be ignored in a pattern and cannot be used in expressions
```

Although pattern matching allows us to build powerful constructs, its usage is limited. For instance, you cannot make function calls on the left side of a match. The following example is invalid:

```
iex> length([1, [2], 3]) = 3
** (CompileError) iex:1: cannot invoke remote function :erlang.length/1 inside match
```

This finishes our introduction to pattern matching. As we will see in the next chapter, pattern matching is very common in many language constructs.