# Structures
[[C]]
---

C structures are special, large variables which contain several named variables inside. Structures are the basic foundation for objects and classes in C. Structures are used for:

-   Serialization of data
-   Passing multiple arguments in and out of functions through a single argument
-   Data structures such as linked lists, binary trees, and more

The most basic example of structures are **points**, which are a single entity that contains two variables - `x` and `y`. Let's define a point:

```c
struct point {
    int x;
    int y;
};
```

Now, let's define a new point, and use it. Assume the function `draw` receives a point and draws it on a screen. Without structs, using it would require two arguments - each for every coordinate:

```c
/* draws a point at 10, 5 */
int x = 10;
int y = 5;
draw(x, y);
```

Using structs, we can pass a point argument:

```c
/* draws a point at 10, 5 */
struct point p;
p.x = 10;
p.y = 5;
draw(p);
```

To access the point's variables, we use the dot `.` operator.

### Typedefs

Typedefs allow us to define types with a different name - which can come in handy when dealing with structs and pointers. In this case, we'd want to get rid of the long definition of a point structure. We can use the following syntax to remove the `struct` keyword from each time we want to define a new point:

```c
typedef struct {
    int x;
    int y;
} point;
```

This will allow us to define a new point like this:

```c
point p;
```

Structures can also hold pointers - which allows them to hold strings, or pointers to other structures as well - which is their real power. For example, we can define a vehicle structure in the following manner:

```c
typedef struct {
    char * brand;
    int model;
} vehicle;
```

Since brand is a char pointer, the vehicle type can contain a string (which, in this case, indicates the brand of the vehicle).

```c
vehicle mycar;
mycar.brand = "Ford";
mycar.model = 2007;
```