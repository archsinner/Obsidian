# Static
[[C]]
---

`static` is a keyword in the C programming language. It can be used with variables and functions.

### What is a static variable?

By default, variables are local to the scope in which they are defined. Variables can be declared as static to increase their scope up to file containing them. As a result, these variables can be accessed anywhere inside a file.

Consider the following scenario – we want to count the runners participating in a race:

```c
[[include]]<stdio.h>
int runner() {
    int count = 0;
    count++;
    return count;
}

int main()
{
    printf("%d ", runner());
    printf("%d ", runner());
    return 0;
}
```

We will see that `count` is not updated because it is removed from memory as soon as the function completes. If `static` is used, however:

```c
[[include]]<stdio.h>
int runner()
{
    static int count = 0;
    count++;
    return count;
}

int main()
{
    printf("%d ", runner());
    printf("%d ", runner());
    return 0;
}
```

### What is a static function?

By default, functions are global in C. If we declare a function with `static`, the scope of that function is reduced to the file containing it.

The syntax looks like this:

```c
static void fun(void) {
   printf("I am a static function.");
}
```

### Static vs Global?

While static variables have scope over the file containing them making them accessible only inside a given file, global variables can be accessed outside the file too.