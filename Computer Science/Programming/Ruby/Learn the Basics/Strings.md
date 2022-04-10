# Strings
[[Ruby]]
---

A string is a collection of characters/symbols inside quotation marks. Strings are interpreted by the computer as raw text.

You can use single quotes or double quotes for strings - either one is acceptable.

```ruby
myFirstString = 'I am a string!' #single quotes
mySecondString = "Me too!" #double quotes
```

There are many built-in methods in Ruby for manipulating strings.

`.length` will give you the number of characters in a string.

```ruby
"Hi!".length #is 3
```

`.reverse` will flip the string around.

```ruby
"Hi!".reverse #is !iH
```

`.upcase` will make a string all caps.

```ruby
"Hi!".upcase #is HI!
```

and `.downcase` will make a string all lowercase.

```ruby
"Hi!".downcase #is hi!
```

You can also use many methods at once. They are solved from left to right.

```ruby
"Hi!".downcase.reverse #is !ih
```

If you want to check if one string contains another string, you can use `.include?`.

```ruby
"Happy Birthday!".include?("Happy")
```

The above code evaluates to `true`.