# Hello, World!
[[Scala]]
---

Scala is somewhat similar to Java. In Scala, the main code construct is an object (versus a class in Java). Let's create an object called HelloWorld with a `main` function. The `main` function will simply print out some text.

```scala
object Main {
    def main(args: Array[String]): Unit = {
        println("Some text")
    }
}
```

Scala also has a REPL (read, execute, print, loop) interpreter so you can run the same thing from the scala command line.