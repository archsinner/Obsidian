# Hello World in Ruby
[[Ruby]]
---

One of the most basic tasks in any programming language is to display information to the user. To print something to the console so the user can see it, use `puts`.

```ruby
puts "I will be printed to the console!"
```

Everything between the quotation marks will be printed to the console.

You can use either single (`'`) or double (`"`) quotation marks with `puts`, as long as you are consistent.

Instead of writing `puts`, you can use the shorter form, `p`.

```ruby
p 'Hello world'
```

You can also use `print` to display information. The difference between `puts` and `print` is that when you use the `puts` keyword, Ruby adds a newline(' \n ') at the end. Ruby does not do this with `print`.

```ruby
puts 'Hello World !!!'
Hello World !!!
=> nil

 print 'Hello World !!!'
 Hello World !!!=> nil
```