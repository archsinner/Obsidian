# Manipulating Arrays

---

### Pushing and popping

Arrays can also function as a stack. The `push` and `pop` methods insert and remove variables from the end of an array.

For example, let's create an empty array and push a few variables.

```javascript
var myStack = [];
myStack.push(1);
myStack.push(2);
myStack.push(3);
console.log(myStack);
```

This will print out:

```javascript
1,2,3
```

After pushing variables to the array, we can then pop variables off from the end.

```javascript
console.log(myStack.pop());
console.log(myStack);
```

This will print out the variable we popped from the array, and what's left of the array:

```javascript
3           // the result from myStack.pop()
1,2         // what myStack contains now
```

### Queues using shifting and unshifting

The `unshift` and `shift` methods are similar to `push` and `pop`, only they work from the beginning of the array. We can use the `push` and `shift` methods consecutively to utilize an array as a queue. For example:

```javascript
var myQueue = [];
myQueue.push(1);
myQueue.push(2);
myQueue.push(3);

console.log(myQueue.shift());
console.log(myQueue.shift());
console.log(myQueue.shift());
```

The `shift` keyword will remove the variables of the array in the exact order they were inserted in, and the output will be:

```javascript
1
2
3
```

The `unshift` method is used to insert a variable at the beginning of an array. For example:

```javascript
var myArray = [1,2,3];
myArray.unshift(0);
console.log(myArray);       // will print out 0,1,2,3
```

### Splicing

Splicing arrays in JavaScript removes a certain part from an array to create a new array, made up from the part we took out. For example, if we wanted to remove the five numbers from the following array beginning from the 3rd index, we would do the following:

```javascript
var myArray = [0,1,2,3,4,5,6,7,8,9];
var splice = myArray.splice(3,5);

console.log(splice);        // will print out 3,4,5,6,7
console.log(myArray);       // will print out 0,1,2,8,9
```

After splicing the array, it will only contain the part before and after the splicing. The splice is equal to all the variables between 3 and 7 (inclusive), and the remainder of the array, which contains all variables between 0 and 2 (inclusive), and 8 to 9 (inclusive).