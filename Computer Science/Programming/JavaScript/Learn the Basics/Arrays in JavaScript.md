# Arrays

---

JavaScript can hold an array of variables in an Array object. In JavaScript, an array also functions as a list, a stack or a queue.

To define an array, either use the brackets notation or the Array object notation:

```javascript
var myArray = [1, 2, 3];
var theSameArray = new Array(1, 2, 3);
```

### Addressing

We can use the brackets `[]` operator to address a specific cell in our array. Addressing uses zero-based indices, so for example, in `myArray` the 2nd member can be addressed with index 1. One of the benefits of using an array datastructure is that you have constant time look-up, if you already know the index of the element you are trying to access.

```javascript
console.log(myArray[1]);      // prints out 2
```

Arrays in JavaScript are sparse, meaning that we can also assign variables to random locations even though previous cells were undefined. For example:

```javascript
var myArray = []
myArray[3] = "hello"
console.log(myArray);
```

Will print out:

```javascript
[undefined, undefined, undefined, "hello"]
```

### Array Elements

Because JavaScript Arrays are just special kinds of objects, you can have elements of different types stored together in the same array. The example below is an array with a string, a number, and an empty object.

```javascript
var myArray = ["string", 10, {}]
```