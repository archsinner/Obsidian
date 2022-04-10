Getting Started
[[Elixir]]
# Binaries, strings, and charlists
1.  [[Unicode and Code Points]]
2.  [[UTF-8 and Encodings]]
3. [[Bitstrings]]
4.  [[Binaries]]
5.  [[Charlists]]

In “Basic types”, we learned a little bit about strings and we used the `is_binary/1` function for checks:

```
iex> string = "hello"
"hello"
iex> is_binary(string)
true
```

In this chapter, we will gain clarity on what exactly binaries are, how they relate to strings, and what single-quoted values, `'like this'`, mean in Elixir. Although strings are one of the most common data types in computer languages, they are subtly complex and are often misunderstood. To understand strings in Elixir, we have to educate ourselves about [Unicode](https://en.wikipedia.org/wiki/Unicode) and character encodings, specifically the [UTF-8](https://en.wikipedia.org/wiki/UTF-8) encoding.