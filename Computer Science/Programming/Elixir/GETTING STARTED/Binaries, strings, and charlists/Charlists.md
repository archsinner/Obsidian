## Charlists
[[Binaries, strings, and charlists]]

Our tour of our bitstrings, binaries, and strings is nearly complete, but we have one more data type to explain: the charlist.

**A charlist is a list of integers where all the integers are valid code points.** In practice, you will not come across them often, except perhaps when interfacing with Erlang, in particular when using older libraries that do not accept binaries as arguments.

Whereas strings (i.e. binaries) are created using double-quotes, charlists are created with single-quoted literals:

```
iex> 'hello'
'hello'
iex> [?h, ?e, ?l, ?l, ?o]
'hello'
```

You can see that instead of containing bytes, a charlist contains integer code points. However, the list is only printed in single-quotes if all code points are within the ASCII range:

```
iex> 'hełło'
[104, 101, 322, 322, 111]
iex> is_list('hełło')
true
```

Interpreting integers as code points may lead to some surprising behavior. For example, if you are storing a list of integers that happen to range between 0 and 127, by default IEx will interpret this as a charlist and it will display the corresponding ASCII characters.

```
iex> heartbeats_per_minute = [99, 97, 116]
'cat'
```

You can convert a charlist to a string and back by using the `to_string/1` and `to_charlist/1` functions:

```
iex> to_charlist("hełło")
[104, 101, 322, 322, 111]
iex> to_string('hełło')
"hełło"
iex> to_string(:hello)
"hello"
iex> to_string(1)
"1"
```

Note that those functions are polymorphic - not only do they convert charlists to strings, they also operate on integers, atoms, and so on.

String (binary) concatenation uses the `<>` operator but charlists, being lists, use the list concatenation operator `++`:

```
iex> 'this ' <> 'fails'
** (ArgumentError) expected binary argument in <> operator but got: 'this '
    (elixir) lib/kernel.ex:1821: Kernel.wrap_concatenation/3
    (elixir) lib/kernel.ex:1808: Kernel.extract_concatenations/2
    (elixir) expanding macro: Kernel.<>/2
    iex:1: (file)
iex> 'this ' ++ 'works'
'this works'
iex> "he" ++ "llo"
** (ArgumentError) argument error
    :erlang.++("he", "llo")
iex> "he" <> "llo"
"hello"
```

With binaries, strings, and charlists out of the way, it is time to talk about key-value data structures.