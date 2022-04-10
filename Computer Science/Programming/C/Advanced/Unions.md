# Unions
[[C]]
---

C Unions are essentially the same as C Structures, except that instead of containing multiple variables each with their own memory a Union allows for multiple names to the same variable. These names can treat the memory as different types (and the size of the union will be the size of the largest type, + any padding the compiler might decide to give it)

So if you wanted to be able to read a variable's memory in different ways, for example read an integer one byte at a time, you could have something like this:

```c
union intParts {
  int theInt;
  char bytes[sizeof(int)];
};
```

Allowing you to look at each byte individually without casting a pointer and using pointer arithmetic:

```c
union intParts parts;
parts.theInt = 5968145; // arbitrary number > 255 (1 byte)

printf("The int is %i\nThe bytes are [%i, %i, %i, %i]\n",
parts.theInt, parts.bytes[0], parts.bytes[1], parts.bytes[2], parts.bytes[3]);

// vs

int theInt = parts.theInt;
printf("The int is %i\nThe bytes are [%i, %i, %i, %i]\n",
theInt, *((char*)&theInt+0), *((char*)&theInt+1), *((char*)&theInt+2), *((char*)&theInt+3));

// or with array syntax which can be a tiny bit nicer sometimes

printf("The int is %i\nThe bytes are [%i, %i, %i, %i]\n",
    theInt, ((char*)&theInt)[0], ((char*)&theInt)[1], ((char*)&theInt)[2], ((char*)&theInt)[3]);
```

Combining this with a structure allows you to create a "tagged" union which can be used to store multiple different types, one at a time.

For example, you might have a "number" struct, but you don't want to use something like this:

```c
struct operator {
    int intNum;
    float floatNum;
    int type;
    double doubleNum;
};
```

Because your program has a lot of them and it takes a bit too much memory for all of the variables, so you could use this:

```c
struct operator {
    int type;
    union {
      int intNum;
      float floatNum;
      double doubleNum;
    } types;
};
```

Like this the size of the struct is just the size of the int `type` + the size of the largest type in the union (the double). Not a huge gain, only 8 or 16 bytes, but the concept can be applied to similar structs.

use:

```c
operator op;
op.type = 0; // int, probably better as an enum or macro constant
op.types.intNum = 352;
```

Also, if you don't give the union a name then it's members are accessed directly from the struct:

```c
struct operator {
    int type;
    union {
        int intNum;
        float floatNum;
        double doubleNum;
    }; // no name!
};

operator op;
op.type = 0; // int
// intNum is part of the union, but since it's not named you access it directly off the struct itself
op.intNum = 352;
```

Another, perhaps more useful feature, is when you always have multiple variables of the same type, and you want to be able to use both names (for readability) and indexes (for ease of iteration), in that case you can do something like this:

```c
union Coins {
    struct {
        int quarter;
        int dime;
        int nickel;
        int penny;
    }; // anonymous struct acts the same way as an anonymous union, members are on the outer container
    int coins[4];
};
```

In that example you can see that there is a struct which contains the four (common) coins in the United States.

since the union makes the variables share the same memory the coins array matches with each int in the struct (in order):

```c
union Coins change;
for(int i = 0; i < sizeof(change) / sizeof(int); ++i)
{
    scanf("%i", change.coins + i); // BAD code! input is always suspect!
}
printf("There are %i quarters, %i dimes, %i nickels, and %i pennies\n",
    change.quarter, change.dime, change.nickel, change.penny);
```