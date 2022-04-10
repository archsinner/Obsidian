# While loops

---

While loops are simple blocks that execute repeatedly until the while loop condition is not met.

Here is an example of a loop that is executed a total of 10 times:

```php
$counter = 0;

while ($counter < 10) {
    $counter += 1;
    echo "Executing - counter is $counter.\n";
}
```

The main difference between for loops and while loops is that for loops are used to iterate over an array or an object, and a while loop will execute an unknown amount of times, depending on variable conditions (for example, until a user has entered the correct input).

### Flow statements

Loops can be controlled using the `break` and `continue` flow statements, which come in handy in while loops very much. The `break` statement immediately quits the for loop at the middle of the block, while the `continue` statement returns to the top of the `while` loop, re-checking if the loop condition is met as well.

#### The continue statement

Let's use the previous example, but this time let's add a check to see if the number is even. If it is, we will skip it, so that only odd numbers will be printed out.

```php
$counter = 0;

while ($counter < 10) {
    $counter += 1;

    if ($counter % 2 == 0) {
        echo "Skipping number $counter because it is even.\n";
        continue;
    }

    echo "Executing - counter is $counter.\n";
}
```

#### The break statement

Let's assume we want to add another test that checks if the counter variable is no larger than 8. If it is, we would like to stop the loop. This will cause the number 9 to be not printed in this example.

```php
$counter = 0;

while ($counter < 10) {
    $counter += 1;

    if ($counter > 8) {
        echo "counter is larger than 8, stopping the loop.\n";
        break;
    }

    if ($counter % 2 == 0) {
        echo "Skipping number $counter because it is even.\n";
        continue;
    }

    echo "Executing - counter is $counter.\n";
}
```

## Exercise

Use a `while` loop to print all **odd** numbers in an array. Use the `continue` statement to skip loops and avoid printing even numbers.

Remember - you will need to use the `\n` character sequence at the end of the echo statement to continue to the next line.

**Tip:** to test whether a number is even, check if the number modulus 2 is equal to zero ($number % 2 == 0).