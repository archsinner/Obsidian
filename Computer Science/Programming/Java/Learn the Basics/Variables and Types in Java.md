# Variables and Types
[[Java]]
---

Although Java is object oriented, not all types are objects. It is built on top of basic variable types called primitives.

Here is a list of all primitives in Java:

-   `byte` (number, 1 byte)
-   `short` (number, 2 bytes)
-   `int` (number, 4 bytes)
-   `long` (number, 8 bytes)
-   `float` (float number, 4 bytes)
-   `double` (float number, 8 bytes)
-   `char` (a character, 2 bytes)
-   `boolean` (true or false, 1 byte)

Java is a strong typed language, which means variables need to be defined before we use them.

### Numbers

To declare and assign a number use the following syntax:

```java
int myNumber;
myNumber = 5;
```

Or you can combine them:

```java
int myNumber = 5;
```

To define a double floating point number, use the following syntax:

```java
double d = 4.5;
d = 3.0;
```

If you want to use float, you will have to cast:

```java
float f = (float) 4.5;
```

Or, You can use this:

```java
float f = 4.5f; // (f is a shorter way of casting float)
```

### Characters and Strings

In Java, a character is it's own type and it's not simply a number, so it's not common to put an ascii value in it, there is a special syntax for chars:

```java
char c = 'g';
```

`String` is not a primitive. It's a real type, but Java has special treatment for String.

Here are some ways to use a string:

```java
// Create a string with a constructor
String s1 = new String("Who let the dogs out?");        // String object stored in heap memory
// Just using "" creates a string, so no need to write it the previous way.
String s2 = "Who who who who!";                         // String literal stored in String pool
// Java defined the operator + on strings to concatenate:
String s3 = s1 + s2;
```

There is no operator overloading in Java but there is the exception that proves the rule - string is the only class where operator overloading is supported. We can concat two strings using + operator. The operator `+` is only defined for strings, you will never see it with other objects, only primitives.

You can also concat string to primitives:

```java
int num = 5;
String s = "I have " + num + " cookies"; //Be sure not to use "" with primitives.
```

### boolean

Every comparison operator in java will return the type boolean. Unlike other languages, it only accepts two special values: `true` or `false`.

```java
boolean b = false;
b = true;

boolean toBe = false;
b = toBe || !toBe;
if (b) {
    System.out.println(toBe);
}

int children = 0;
b = children; // Will not work
if (children) { // Will not work
    // Will not work
}

int a;
boolean b = true; 
boolean c = false; 
a = b + c;            //The following line will give an error
System.out.println(a);
```