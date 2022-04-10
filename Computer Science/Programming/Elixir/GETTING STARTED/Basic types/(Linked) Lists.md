## (Linked) Lists
[[Basic types]]

Elixir uses square brackets to specify a list of values. Values can be of any type:

```
iex> [1, 2, true, 3]
[1, 2, true, 3]
iex> length [1, 2, 3]
3
```

Two lists can be concatenated or subtracted using the `++/2` and `--/2` operators respectively:

```
iex> [1, 2, 3] ++ [4, 5, 6]
[1, 2, 3, 4, 5, 6]
iex> [1, true, 2, false, 3, true] -- [true, false]
[1, 2, 3, true]
```

List operators never modify the existing list. Concatenating to or removing elements from a list returns a new list. We say that Elixir data structures are _immutable_. One advantage of immutability is that it leads to clearer code. You can freely pass the data around with the guarantee no one will mutate it in memory - only transform it.

Throughout the tutorial, we will talk a lot about the head and tail of a list. The head is the first element of a list and the tail is the remainder of the list. They can be retrieved with the functions `hd/1` and `tl/1`. Let’s assign a list to a variable and retrieve its head and tail:

```
iex> list = [1, 2, 3]
iex> hd(list)
1
iex> tl(list)
[2, 3]
```

Getting the head or the tail of an empty list throws an error:

```
iex> hd([])
** (ArgumentError) argument error
```

Sometimes you will create a list and it will return a value in single quotes. For example:

```
iex> [11, 12, 13]
'\v\f\r'
iex> [104, 101, 108, 108, 111]
'hello'
```

When Elixir sees a list of printable ASCII numbers, Elixir will print that as a charlist (literally a list of characters). Charlists are quite common when interfacing with existing Erlang code. Whenever you see a value in IEx and you are not quite sure what it is, you can use the `i/1` to retrieve information about it:

```
iex> i 'hello'
Term
  'hello'
Data type
  List
Description
  ...
Raw representation
  [104, 101, 108, 108, 111]
Reference modules
  List
Implemented protocols
  ...
```

Keep in mind single-quoted and double-quoted representations are not equivalent in Elixir as they are represented by different types:

```
iex> 'hello' == "hello"
false
```

Single quotes are charlists, double quotes are strings. We will talk more about them in the [“Binaries, strings and charlists”](https://elixir-lang.org/getting-started/binaries-strings-and-char-lists.html) chapter.