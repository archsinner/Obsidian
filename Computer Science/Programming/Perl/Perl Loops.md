# Loops

---

Like many programming languages Perl offers several loop structures. A **loop** allows you to execute statement blocks over and over again, with logical conditions, value lists or control statements being used to control the loop.

The basic loop structures are:

`while CONDITION {BLOCK}`: repeat a BLOCK while the CONDITION is true. The CONDITION is evaluated before executing the BLOCK.

```perl
$count = 10;
while ($count > 0) {
  print "Countdown is: $count\n";
  $count--;
}
```

`until CONDITION {BLOCK}`: repeat a BLOCK until the CONDITION is true. The CONDITION is evaluated before executing the BLOCK.

```perl
$count = 1;
until ($count > 10) {
  print "Countup is: $count\n";
  $count++;
}
```

`for (INIT ; CONDITION ; COMMAND) {BLOCK}`: This is a loop structure similar to the C language `for` loop. Before the loop starts execute INIT as the initialization sequence. Then repeat the statement BLOCK while CONDITION is true. CONDITION is tested before executing BLOCK. After each iteration, execute the COMMAND.

```perl
for ($count = 1 ; $count < 10 ; $count++) {
  print "My count is: $count\n";
}
```

`foreach VAR (ARRAY) {BLOCK}`: iterate over all ARRAY values, assigning VAR to the next value from ARRAY in each iteration, and run BLOCK for each value.

```perl
@colors = ('red', 'blue', 'yellow');
foreach $color (@colors) {
    print "Color: $color\n";
}
```

`do BLOCK while CONDITION`: repeat a statement BLOCK while CONDITION is true. CONDITION is tested after executing BLOCK.

```perl
$count = 10;
do {
  print "Countdown is: $count\n";
  $count--;
} while ($count > 0)
```

## Loop Control Statements

Loop control statements can be placed within the loop's statement BLOCK. When executed, these will alter the normal loop sequence. Some useful control statements are:

-   `next` causes the loop to skip the rest of the statement block (like `continue` in the C language)
-   `last` causes the loop to skip the rest of the statement block and exit the loop iterations (like `break` in the C language)

For example:

```perl
@colors = ('red', 'blue', 'yellow', 'pink', 'black');
foreach $color (@colors) {
    if ($color eq 'blue') {
        next;
    }
    print "Color: $color\n";
    if ($color eq 'pink')  {
        last;
    }
}
print "Exited loop!";
```

Perl supports loop nesting. This means that statement blocks may include loop structures.

A loop becomes an infinite loop when its condition is always false.

## Exercise

In this exercise, you will need to loop through and print out all even numbers from the `@NUMBERS` array in the same order they are received. Don't print any numbers that come after 237 in the array.

 Start Exercise