# Object Oriented JavaScript

---

JavaScript uses functions as classes to create objects using the `new` keyword. Here is an example:

```javascript
function Person(firstName, lastName) {
    // construct the object using the arguments
    this.firstName = firstName;
    this.lastName = lastName;

    // a method which returns the full name
    this.fullName = function() {
        return this.firstName + " " + this.lastName;
    }
}

var myPerson = new Person("John", "Smith");
console.log(myPerson.fullName());            // outputs "John Smith"
```

Creating an object using the `new` keyword is the same as writing the following code:

```javascript
var myPerson = {
    firstName : "John",
    lastName : "Smith",
    fullName : function()
    {
        return this.firstName + " " + this.lastName;
    }
}
```

The difference between the two methods of creating objects is that the first method uses a class to define the object and then the `new` keyword to instantiate it, and the second method immediately creates an instance of the object.