# Functions

---

Functions are simple code blocks we can call from anywhere. For example, we can create a function that sums a list of numbers and returns the result. Let's call this function `sum`.

There are two types of functions - library functions and user functions. Library functions, such as `array_push` are part of the PHP library and can be used by anyone. However, you may write your own functions and use them across your code.

A function receives a list of arguments separated by commas. Every argument only exists in the context of the function, meaning that they become variables inside the function block, but are not defined outside of that function block.

```php
// define a function called `sum` that will
// receive a list of numbers as an argument.
function sum($numbers) {
    // initialize the variable we will return
    $sum = 0;

    // sum up the numbers
    foreach ($numbers as $number) {
        $sum += $number;
    }

    // return the sum to the user
    return $sum;
}

// Example usage of sum
echo sum([1,2,3,4,5,6,7,8,9,10]);
```

After defining functions, you may load other PHP files into one another, so you may define all your functions in one file, and load them for another. Let's say that we have defined the `sum` function inside a file called `sum.php`. We can now create another file, say `index.php` and use the `sum` function by including `sum.php` as follows:

```php
include("sum.php");

// Example usage of sum
echo sum([1,2,3,4,5,6,7,8,9,10]);
```

(This code will not run because there are no modules defined in the PHP environment).

## Exercise

Create a function `squared_sum` that returns the sum of every integer in an array, squared.