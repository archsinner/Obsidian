# Try and Catch
[[Java]]
---

Before going into try/catch statements, let's talk about Exceptions. Exceptions are thrown every time an error occurs. Some examples: _ArrayIndexOutOfBounds is thrown if the index that does not exist in an array is accessed (e.g: Trying to access arr[5], but arr only goes up to arr[4])_ ArithmeticError is thrown if an illegal arithmetic operation is done (e.g: 42/0, division by zero)

There are lots of exceptions that Java can throw (more than the above).

But, how can you handle exceptions, when you're unsure if an error will occur.

That's the purpose of try/catch! This is the syntax for try/catch:

```java
  try {
    //Code here
  } catch (ExceptionHere name) {
        //Replace ExceptionHere with your exception and name with the name of your exception.
        //Code if exception "ExceptionHere" is thrown.
  }
```

The code after the try block will be attempted to be run. If the exception in the catch statement is thrown during the code in the try block is run, run the code in the catch block.

You can tell the user that there is a problem, or anything else.

NOTE: You can also use Exception as the exception to catch if any exception is thrown.