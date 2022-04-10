# Using Generics
[[Java]]
---

Generics provide compile-time type safety that allows programmers to catch invalid types at compile time.

As this feature is often used with collections, we will focus on collections. Generics allows the user to set the type of the collection to limit what kind of objects can be inserted into the collection. The user also does not have to cast the values obtain from the collection.

When declaring a generic, it must have a type parameter specifying what type of elements will be in the collection. For example, to declare a list containing strings, you would write:

```java
List<String> names = new ArrayList<>();
```

### Generics in class declaration

You can also use generics for class definition:

```java
public class YourClass<Class1,Class2>{
    private Class1 bob1;
    private Class2 bob2;
    Abc(Class1 a, Class2 b){
        this.bob1 = a;
        this.bob2 = b;
    }
    public Class1 getBob1() {
        return (this.bob1);
    }
    public Class2 getBob2() {
        return (this.bob2);
    }
}
```

This is usefull when you want to have multiple options for classes of variables in your class, but don't want to write new constructors and functions for every single type. Now you can just run:

```java
YourClass<String, Integer> leBobs = new YourClass<>("words",42);  //in this case, <> is the same as putting <String, Integer>
String a=leBobs.getBob1();
int b=leBobs.getBob2();
System.out.println("bob1 is '" + a + "', and bob2 is '" + b + "'.");
```

To change the types of `bob1` and `bob2` just change the classes in the `<>` when you declare an object of the class `YourClass`.

Note: you cannot use primitives for generics unless you use their class version: ie <~~int~~ Integer> or <~~bool~~ Boolean>