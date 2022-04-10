## Strings
[[Basic types]]

Strings in Elixir are delimited by double quotes, and they are encoded in UTF-8:

```
iex> "hellö"
"hellö"
```

> Note: if you are running on Windows, there is a chance your terminal does not use UTF-8 by default. You can change the encoding of your current session by running `chcp 65001` before entering IEx.

Elixir also supports string interpolation:

```
iex> string = :world
iex> "hellö #{string}"
"hellö world"
```

Strings can have line breaks in them. You can introduce them using escape sequences:

```
iex> "hello
...> world"
"hello\nworld"
iex> "hello\nworld"
"hello\nworld"
```

You can print a string using the `IO.puts/1` function from the `IO` module:

```
iex> IO.puts("hello\nworld")
hello
world
:ok
```

Notice that the `IO.puts/1` function returns the atom `:ok` after printing.

Strings in Elixir are represented internally by contiguous sequences of bytes known as binaries:

```
iex> is_binary("hellö")
true
```

We can also get the number of bytes in a string:

```
iex> byte_size("hellö")
6
```

Notice that the number of bytes in that string is 6, even though it has 5 graphemes. That’s because the grapheme “ö” takes 2 bytes to be represented in UTF-8. We can get the actual length of the string, based on the number of graphemes, by using the `String.length/1` function:

```
iex> String.length("hellö")
5
```

The [String module](https://hexdocs.pm/elixir/String.html) contains a bunch of functions that operate on strings as defined in the Unicode standard:

```
iex> String.upcase("hellö")
"HELLÖ"
```