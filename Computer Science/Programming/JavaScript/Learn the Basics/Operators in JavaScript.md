# Operators in JavaScript

---

Every variable in JavaScript is casted automatically so any operator between two variables will always give some kind of result.

### The addition operator

The `+` (addition) operator is used for both addition and concatenation of strings.

For example, adding two variables is easy:

```javascript
var a = 1;
var b = 2;
var c = a + b;     // c is now equal to 3
```

The addition operator is used for concatenating strings to strings, strings to numbers, and numbers to strings:

```javascript
var name = "John";
console.log("Hello " + name + "!");
console.log("The meaning of life is " + 42);
console.log(42 + " is the meaning of life");
```

JavaScript behaves differently when you are trying to combine two operands of different types. The default primitive value is a string, so when you try to add a number to a string, JavaScript will transform the number to a string before the concatenation.

```javascript
console.log(1 + "1");   // outputs "11"
```

### Mathematical operators

To subtract, multiply and divide two numbers, use the minus (`-`), asterisk (`*`) and slash (`/`) signs.

```javascript
console.log(3 - 5);     // outputs -2
console.log(3 * 5);     // outputs 15
console.log(3 / 5);     // outputs 0.6
```

### Advanced mathematical operators

JavaScript supports the modulus operator (`%`) which calculates the remainder of a division operation.

```javascript
console.log(5 % 3);     // outputs 2
```

JavaScript also supports combined assignment and operation operators. So, instead of typing `myNumber = myNumber / 2`, you can type `myNumber /= 2`. Here is a list of all these operators:

-   `/=`
-   `*=`
-   `-=`
-   `+=`
-   `%=`

JavaScript also has a `Math` module which contains more advanced functions:

-   `Math.abs` calculates the absolute value of a number
-   `Math.exp` calculates **e** to the power of a number
-   `Math.pow(x,y)` calculates the result of **x** to the power of **y**
-   `Math.floor` removes the fraction part from a number
-   `Math.random()` will give a random number `x` where 0<=x<1

And many more mathematical functions.