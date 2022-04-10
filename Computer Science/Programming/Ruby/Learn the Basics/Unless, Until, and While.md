# Unless, Until, and While
[[Ruby]]
---

The `unless` statement is structured similarly to an `if` statement.

```ruby
unless condition
  #thing to be done if the condition is false
end
```

It is basically the reverse of the if statement, because `if` statements will only be done if the condition is `true`, but the `unless` statement will only be done if the condition is `false`. The `else` keyword can also be used inside `unless` statements.

`while` statements repeat a block of code as long as a condition is `true`.

```ruby
while condition
    #something to do
end
```

`until` statements are the opposite of `while` statements; they repeat until a condition becomes `true`. Here is their syntax:

```ruby
until condition
    #something to do
end
```

### Important!

Make sure that you don't make an **infinite loop**. An infinite loop repeats forever, stopping your program from ever advancing, because the condition never changes to what will stop the loop.