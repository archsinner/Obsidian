# Hashes and Symbols
[[Ruby]]
---

Just like arrays, hashes allow you to store multiple values together. However, while arrays store values with a numerical index, hashes store information using key-value pairs. Each piece of information in the hash has a unique label, and you can use that label to access the value.

To create a hash, use `Hash.new`, or `myHash={}`. For example:

```ruby
myHash={
    "Key" => "value",
    "Key2" => "value2"
}
```

This creates a hash with two values, each one indexed with a key. You can access a value like so:

```ruby
puts myHash["Key"] # puts value
```

The other method of creating a hash is shown below:

```ruby
myHash=Hash.new()
myHash["Key"]="value"
myHash["Key2"]="value2"
```

Instead of using a string as a key, you can also use a symbol, like this:

```ruby
myHash=Hash.new()
myHash[:Key]="value"
myHash[:Key2]="value2"
```

You can access a value keyed to a symbol in the same way.

```ruby
puts myHash[:Key] # puts "value"
```

When using `myHash={}` with symbols, symbols are used differently, like this

```ruby
myHash={
    Key: "value",
    Key2: "value2",
}
puts myHash[:Key] # puts "value"
```