## UTF-8 and Encodings
[[Binaries, strings, and charlists]]

Now that we understand what the Unicode standard is and what code points are, we can finally talk about encodings. Whereas the code point is **what** we store, an encoding deals with **how** we store it: encoding is an implementation. In other words, we need a mechanism to convert the code point numbers into bytes so they can be stored in memory, written to disk, etc.

Elixir uses UTF-8 to encode its strings, which means that code points are encoded as a series of 8-bit bytes. UTF-8 is a **variable width** character encoding that uses one to four bytes to store each code point. It is capable of encoding all valid Unicode code points. Let’s see an example:

```
iex> string = "héllo"
"héllo"
iex> String.length(string)
5
iex> byte_size(string)
6
```

Although the string above has 5 characters, it uses 6 bytes, as two bytes are used to represent the character `é`.

> Note: if you are running on Windows, there is a chance your terminal does not use UTF-8 by default. You can change the encoding of your current session by running `chcp 65001` before entering `iex` (`iex.bat`).

Besides defining characters, UTF-8 also provides a notion of graphemes. Graphemes may consist of multiple characters that are often perceived as one. For example, `é` can be represented in Unicode as a single character. It can also be represented as the combination of the character `e` and the acute accent character `´` into a single grapheme. We can use the function `String.normalize/2` to get the composed (usualy the default in most systems) and the decomposed representation of a string. Let’s force the composed (`:nfc`) representation first:

```
iex> composed = String.normalize("é", :nfc)
"é"
iex> String.codepoints(composed)
["é"]
iex> String.graphemes(composed)
["é"]
```

Now the decomposed (`:nfd`) version:

```
iex> decomposed = String.normalize("é", :nfd)
"é"
iex> String.codepoints(decomposed)
["e", "́"]
iex> String.graphemes(decomposed)
["é"]
```

Even though they are visually the same, the decomposed version is made of two characters, where the acute accent `´` is its own character.

Although these rules may sound complicated, UTF-8 encoded documents are everywhere. This page itself is encoded in UTF-8. The encoding information is given to your browser which then knows how to render all of the bytes, characters, and graphemes accordingly.

A common trick in Elixir when you want to see the inner binary representation of a string is to concatenate the null byte `<<0>>` to it:

```
iex> "hełło" <> <<0>>
<<104, 101, 197, 130, 197, 130, 111, 0>>
```

Alternatively, you can view a string’s binary representation by using [IO.inspect/2](https://hexdocs.pm/elixir/IO.html#inspect/2):

```
iex> IO.inspect("hełło", binaries: :as_binaries)
<<104, 101, 197, 130, 197, 130, 111>>
```

We are getting a little bit ahead of ourselves. Let’s talk about bitstrings to learn about what exactly the `<<>>` constructor means.