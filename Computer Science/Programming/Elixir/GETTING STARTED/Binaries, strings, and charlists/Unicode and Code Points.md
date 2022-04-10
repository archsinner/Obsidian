## Unicode and Code Points
[[Binaries, strings, and charlists]]

In order to facilitate meaningful communication between computers across multiple languages, a standard is required so that the ones and zeros on one machine mean the same thing when they are transmitted to another. The [Unicode Standard](https://unicode.org/standard/standard.html) acts as an official registry of virtually all the characters we know: this includes characters from classical and historical texts, emoji, and formatting and control characters as well.

Unicode organizes all of the characters in its repertoire into code charts, and each character is given a unique numerical index. This numerical index is known as a [Code Point](https://en.wikipedia.org/wiki/Code_point).

In Elixir you can use a `?` in front of a character literal to reveal its code point:

```
iex> ?a
97
iex> ?ł
322
```

Note that most Unicode code charts will refer to a code point by its hexadecimal representation, e.g. `97` translates to `0061` in hex, and we can represent any Unicode character in an Elixir string by using the `\u` notation and the hex representation of its code point number:

```
iex> "\u0061" === "a"
true
iex> 0x0061 = 97 = ?a
97
```

The hex representation will also help you look up information about a code point, e.g. [https://codepoints.net/U+0061](https://codepoints.net/U+0061) has a data sheet all about the lower case `a`, a.k.a. code point 97.