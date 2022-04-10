# Generic Types
[[Java]]
---

Java Generic methods and generic classes enable programmers to specify, with a single method declaration, a set of related methods, or with a single class declaration, a set of related types, respectively.Generic in java is similar to templates in C++. It allows the user to parameterized the types in classes, or interface. The user have to <> to specify parameter types in generic class creation.

## Generic Methods

public methodName() { ... }

## Generic class

public class ClassName { ... }

## Generic variable

T varibaleName;

Lets see a code sample to easily understand the generic types.

//This a Generic class declaration class Generic // This class accepts any data type {

// Generic variable declaration T variable; public Generic(T variable) // constructor for generic class { this.variable = variable; }

//generic method declaration public getVariable() // method to get the variable of generic type { return variable; } }

This the main class where the object for generic class is created here.

```java
class Main
{
    public static void main(String args[])
    {
```

// Here the object is created for the generic class Generic intvar = new Generic(20); // Here the object is created for Generic class of type Integer. System.out.println(intvar.getVariable());

```java
        Generic<String> strvar = new Generic<String>("I love Java"); // Here the object is created for Generic class of type String.
        System.out.println(strvar.getVariable());

    }

}
```

## OUTPUT

20  
I love Java

The code shows you that the class constructor while object creation can accept any data type.