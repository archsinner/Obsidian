## Bitstrings
[[Binaries, strings, and charlists]]

Although we have covered code points and UTF-8 encoding, we still need to go a bit deeper into how exactly we store the encoded bytes, and this is where we introduce the **bitstring**. A bitstring is a fundamental data type in Elixir, denoted with the `<<>>` syntax. **A bitstring is a contiguous sequence of bits in memory.**

A complete reference about the binary / bitstring constructor `<<>>` can be found [in the Elixir documentation](https://hexdocs.pm/elixir/Kernel.SpecialForms.html#%3C%3C%3E%3E/1).

By default, 8 bits (i.e. 1 byte) is used to store each number in a bitstring, but you can manually specify the number of bits via a `::n` modifier to denote the size in `n` bits, or you can use the more verbose declaration `::size(n)`:

```
iex> <<42>> === <<42::8>>
true
iex> <<3::4>>
<<3::size(4)>>
```

For example, the decimal number `3` when represented with 4 bits in base 2 would be `0011`, which is equivalent to the values `0`, `0`, `1`, `1`, each stored using 1 bit:

```
iex> <<0::1, 0::1, 1::1, 1::1>> == <<3::4>>
true
```

Any value that exceeds what can be stored by the number of bits provisioned is truncated:

```
iex> <<1>> === <<257>>
true
```

Here, 257 in base 2 would be represented as `100000001`, but since we have reserved only 8 bits for its representation (by default), the left-most bit is ignored and the value becomes truncated to `00000001`, or simply `1` in decimal.