# Comments
[[Ruby]]
---

As you start to write more complicated programs, it will become necessary to start using comments. Comments allows you to add explanations to your code, so that other developers (and you) can always understand what a particular piece of code is for. It's good practice to comment your code extensively.

There are two types of comments, multi-line comments, and single-line comments. Single-line are started with `#` and multi-line comments are started with `=begin` and ended with `=end`.

```ruby
=begin
I'm a comment!
=end
```

Single-line comments can be started after another thing in the same line.

```ruby
puts "Hi!" [[I]]'m a comment, but Hi! will still be printed to the console.
```