# Bitmasks
[[C]]
---

Bit masking is simply the process of storing data truly as bits, as opposed to storing it as chars/ints/floats. It is incredibly useful for storing certain types of data compactly and efficiently.

The idea for bit masking is based on boolean logic. For those not familiar, boolean logic is the manipulation of 'true' (1) and 'false' (0) through logical operations (that take 0s and 1s as their argument). We are concerned with the following operations:

-   NOT a - the final value is the opposite of the input value (1 -> 0, 0 -> 1)
-   a AND b - if both values are 1, the final value is 1, otherwise the final value is 0
-   a OR b - if either value is 1, the final value is 1, otherwise the final value is 0
-   a XOR b - if one value is 1 and the other value is 0, the final value is 1, otherwise the final value is 0

In computing, one of these true/false values is a _bit_. Primitives in C (`int`, `float`, etc) are made up of some number of bits, where that number is a multiple of 8. For example, an `int` may be at least 16 bits in size, where a `char` may be 8 bits. 8 bits is typically referred to as a _byte_. C guarantees that certain primitives are [at least some number](http://en.wikipedia.org/wiki/C_data_types#Basic_types) of bytes in size. The introduction of `stdint.h` in C11 allows the programmer to specify integer types that are exactly some number of bytes, which is extremely useful when using masks.

Bit masks are often used when setting flags. Flags are values that can be in two states, such as 'on/off' and 'moving/stationary'.

### Setting bit n

Setting bit `n` is as simple as ORing the value of the storage variable with the value `2^n`.

`storage |= 1 << n;`

As an example, here is the setting of bit 3 where `storage` is a char (8 bits):

`01000010 OR 00001000 == 01001010`

The `2^n` logic places the '1' value at the proper bit in the mask itself, allowing access to that same bit in the storage variable.

### Clearing bit n

Clearing bit `n` is the result of ANDing the value of the storage variable with the inverse (NOT) of the value `2^n`:

`storage &= ~(1 << n);`

Here's the example again:

`01001010 AND 11110111 == 01000010`

### Flipping bit n

Flipping bit `n` is the result of XORing the value of the storage variable with `2^n`:

`storage ^= 1 << n;`

`01000010 01001010 XOR XOR 00001000 00001000 == == 01001010 01000010`

### Checking bit n

Checking a bit is ANDing the value of `2^n` with the bit storage:

`bit = storage & (1 << n);`

`01000010 01001010 AND AND 00001000 00001000 == == 00000000 00001000`