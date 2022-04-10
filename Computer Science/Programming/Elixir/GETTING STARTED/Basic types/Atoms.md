## Atoms
[[Basic types]]

An atom is a constant whose value is its own name. Some other languages call these symbols. They are often useful to enumerate over distinct values, such as:

```
iex> :apple
:apple
iex> :orange
:orange
iex> :watermelon
:watermelon
```

Atoms are equal if their names are equal.

```
iex> :apple == :apple
true
iex> :apple == :orange
false
```

Often they are used to express the state of an operation, by using values such as `:ok` and `:error`.

The booleans `true` and `false` are also atoms:

```
iex> true == :true
true
iex> is_atom(false)
true
iex> is_boolean(:false)
true
```

Elixir allows you to skip the leading `:` for the atoms `false`, `true` and `nil`.

Finally, Elixir has a construct called aliases which we will explore later. Aliases start in upper case and are also atoms:

```
iex> is_atom(Hello)
true
```