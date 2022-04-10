# Methods With Parameters
[[Ruby]]
---

To extend the functionality of our methods, we can define them with parameters and provide them with arguments. Parameters are placeholder names we put between the method's parentheses when we define the method and arguments are pieces of code that we put in the method's parentheses when we call the method. Take this example:

```ruby
def clap_hands(number)
    puts "Clap " * number
end
```

In this example, we pass `number` as a parameter. Then within our method, we `puts` the word "Clap " to the console as many times as `number`.

Just like methods that do not have parameters, we need to call the method for it to take effect. So in this example we would call our `clap_hands` method like so:

```ruby
clap_hands(3)
```

This would `puts` the string "Clap " three times to the console. The value of `3` is the argument that we are providing the method.