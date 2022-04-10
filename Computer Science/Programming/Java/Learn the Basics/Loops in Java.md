# Loops
[[Java]]
---

There are two kind of loops in Java, `for` and `while`.

### For

The for loop has three sections:

```java
for (int i = 0; i < 3; i++) {}
```

First section runs once when we enter the loop.

Second section is the gate keeper, if it returns `true`, we run the statements in the loop, if it returns `false`, we exit the loop. It runs right after the first section for the first time, then every time the loop is finished and the third section is run.

The third section is the final statement that will run every time the loop runs.

So in the case we have just seen, the loop will run 3 times. Here is the order of the commands:

```java
int i = 0;
i < 3 // 0 < 3 = true
      // Inside of loop
i++ // i is now 1
i < 3 // 1 < 3 = true
      // Inside of loop
i++ // i is now 2
i < 3 // 2 < 3 = true
      // Inside of loop
i++ // i is now 3
i < 3 // 3 < 3 = false
      // Loop is done...
```

We can omit the first and third section of the loop (although it will be weird), and the loop will still work:

```java
for (;i < 5;) {}
```

For cases where we want to use a loop that look like that, we use a `while` loop

### While

The syntax is very similar to the previous for we looked at:

```java
while (condition) {}
```

The condition will run for the first time when entering and every time the loop is done. If it returns false, the loop will not run.

If we want the loop to always run at least one, we can use do-while

```java
do {

} while(condition);
```

Notice the `;` in the end of the do-while.

### Foreach

Another version of for, is the foreach. The keyword we use is still `for`, but when we want to iterate on the elements inside an array we can simply use it:

```java
int[] arr = {2, 0, 1, 3};
for (int el : arr) {
    System.out.println(el);
}
```

This is a short version and equivalent to:

```java
int[] arr = {1, 9, 9, 5};
for (int i = 0; i < arr.length; i++) {
    int el = arr[i];
    System.out.println(el);
}
```

Notice that if you want to use the index of the element inside the loop, you have to use the longer version and can't use foreach.

### break and continue

These two keywords help us control the loop from within it. `break` will cause the loop to stop and will go immediately to the next statement after the loop:

```java
int i;
for (i = 0; i < 5; i++) {
    if (i >= 2) {
        break;
    }
    System.out.println("Yuhu");
}
System.out.println(i);
// Output:
// Yuhu
// Yuhu
// 2
```

`continue` will stop the current iteration and will move to the next one. Notice that inside a for loop, it will still run the third section.

```java
int i;
for (i = 0; i < 5; i++) {
    if (i >= 3) {
        break;
    }
    System.out.println("Yuhu");
    if (i >= 1) {
        continue;
    }
    System.out.println("Tata");
}
System.out.println(i);
// Output
// Yuhu
// Tata
// Yuhu
// Yuhu
// 3
```