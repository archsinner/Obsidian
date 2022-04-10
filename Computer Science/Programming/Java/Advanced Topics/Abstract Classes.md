# Abstract Classes
[[Java]]
---

An Abstract class is a class which has `abstract` keyword prefixed to it. A class must be prefixed with `abstract` if it has one or more methods with abstract keyword. An abstract method is only declared but not implemented. An abstract class cannot be instanciated but can be inherited by another class. The inheriting class must implement all the abstract methods or else the subclass should also be declared as abstract.

For example:

```java
abstract class abstractClass { 
    abstract void abstractMethod(); 
    void concreteMethod() { // concrete methods are still allowed in abstract classes 
        System.out.println("This is a concrete method."); 
    } 
}
```

### Abstract classes versus interface

Abstract classes can contain fields which are not `final` and `static` and can contain implemented methods as well but interfaces cannot. Abstract classes with only abstract methods should be defined as interfaces.

When an abstract class implements an interface not all interface methods need to be implemented, if the class is not abstract all the interface methods should be implemented.

For example:

```java
abstract class X implements Y {
// implements all but one method of Y
}

class XX extends X {
// implements the remaining method in Y
}
```

Abstract classes can have `static` fields and `static` methods and works it would with normal classes.