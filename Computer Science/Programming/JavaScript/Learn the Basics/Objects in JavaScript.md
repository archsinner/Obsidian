# Objects

---

JavaScript is a functional language, and for object oriented programming it uses both objects and functions, but objects are usually used as a data structure, similar to a dictionary in Python or a map in Java. In this tutorial, we will learn how to use objects as a data structure. The advanced tutorials explain more about object oriented JavaScript.

To initialize an object, use curly braces:

```javascript
var emptyObject = {};
var personObject = {
    firstName : "John",
    lastName : "Smith"
}
```

### Member addressing

Members of objects can be addressed using the brackets operator `[]`, very much like arrays, but just like many other object oriented languages, the period `.` operator can also be used. They are very similar, except for the fact that brackets return a member by using a string, in contrast to the period operator, which requires the member to be a simple word (the word should not contain spaces, start with a number or use illegal characters).

For example, we can continue to fill the person object with more details:

```javascript
var personObject = {
    firstName : "John",
    lastName : "Smith"
}
personObject.age = 23;
personObject["salary"] = 14000;
```

### Iteration

Iterating over members of a dictionary is not a trivial task, since iterating over objects can also yield members who don't actually belong to an object. Therefore, we must use the `hasOwnProperty` method to check that the member in fact belongs to the object.

```javascript
for (var member in personObject)
{
    if (personObject.hasOwnProperty(member))
    {
        console.log("the member " + member + " of personObject is " + personObject[member])
    }
}
```

This will eventually print out

```javascript
the member firstName of personObject is John
the member lastName of personObject is Smith
the member age of personObject is 23
the member salary of personObject is 14000
```

Note that methods of objects in JavaScript have a fixed order, like arrays.