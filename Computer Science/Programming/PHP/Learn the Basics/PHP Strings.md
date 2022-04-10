# Strings

---

Strings are variables that hold text. For example, a string which contains a name is defined as follows:

```php
$name = "John";
echo $name;
```

We can easily format strings using variables. For example:

```php
$name = "John";
$introduction = "Hello $name";
echo $introduction;
```

We can also concatenate strings using the dot `.` operator. For example:

```php
$first_name = "John";
$last_name = "Doe";
$name = $first_name . " " . $last_name;
echo $name;
```

To measure the length of a string, we use the `strlen` function:

```php
$string = "The length of this string is 43 characters.";
echo strlen($string);
```

To cut a part of a string and return it as a new string, we can use the `substr` function:

```php
$filename = "image.png";
$extension = substr($filename, strlen($filename) - 3);
echo "The extension of the file is $extension";
```

### Joining and splitting

We can join arrays to form strings, or split strings to arrays of strings.

For example, to split a string with a list of fruits separated by a comma, we use the `explode` function:

```php
$fruits = "apple,banana,orange";
$fruit_list = explode(",", $fruits);
echo "The second fruit in the list is $fruit_list[1]";
```

To join back an array to a single string separated with commas, we use the `implode` function:

```php
$fruit_list = ["apple","banana","orange"];
$fruits = implode(",", $fruit_list);
echo "The fruits are $fruits";
```

## Exercise

Split string that contains the list of numbers into a new array called number_list.