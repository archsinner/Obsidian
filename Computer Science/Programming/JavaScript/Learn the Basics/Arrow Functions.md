# Arrow Functions

---

Arrow functions are a feature of ES6, their behavior are generally the same of a function. These are anonymous functions with a special syntax, they haven't their own this, arguments or super. They can't be used as constructors too.

Arrow functions are often used as callbacks of native JS functions like map, filter or sort. The reason of their name is due to the use of `=>` in the syntax.

To define an arrow function, we use the `() => {}` structure as follows:

```javascript
const greet = (name) => { return "Hello " + name + "!"; }

console.log(greet("Eric"));      // prints out Hello Eric!
```

In this function, the `name` argument to the `greet` function is used inside the function to construct a new string and return it using the `return` statement.

In case that the function only receives one argument, we can omit the parenthesis:

```javascript
const greet = name => { return "Hello " + name + "!"; }

console.log(greet("Eric"));      // prints out Hello Eric!
```

And, in case that we want to do a explicit return of the function and we have only one line of code, we can avoid the `return` statement and omit brackets too:

```javascript
const greet = name => "Hello " + name + "!";

console.log(greet("Eric"));      // prints out Hello Eric!
```

Using an arrow as a callback compared to a normal function:

```javascript
let numbers = [3, 5, 8, 9, 2];

// Old way
function multiplyByTwo(number){
    return number * 2;
}

let multipliedNumbers = numbers.map(multiplyByTwo);

console.log(multipliedNumbers);              // prints out: 6, 10, 16, 18, 4

// Using ES6 arrow functions
const multiplyByTwo = number => number * 2;

let multipliedNumbers = numbers.map(multiplyByTwo);

console.log(multipliedNumbers);              // prints out: 6, 10, 16, 18, 4
```