# Exceptions
[[Java]]
---

Exceptions are thrown every time an error occurs. The list of all built in exceptions can be accessed at http://docs.oracle.com/javase/7/docs/api/java/lang/Exception.html.

Exceptions are handled using try/catch statements. All code that may throw an exception must follow the Catch or Specify requirement. To follow that requirement, just wrap the code that may throw an error in a try block. If, for some reason, it's not suitable or you cannot use try/catch, you must specify all exceptions a method/function can throw using the `throws` keyword

```java
public void writeFile() throws IOException
```

You can also throw an exception in the code using throw new:

```java
throw new IllegalArgumentException("Number not above 0");
/* Will print 
    Exception in thread "Main": java.lang.IllegalArgumentException: Number not above 0
*/
```

Exceptions are handled using try/catch, which are covered in an earlier lesson:

```java
try {
    System.out.println(arr[10]);
catch (ArrayIndexOutOfBoundsException ex) {
    System.out.println("Error in try block");
}
```