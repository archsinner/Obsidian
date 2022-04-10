# Strings
[[C]]
---

### Defining strings

Strings in C are actually arrays of characters. Although using pointers in C is an advanced subject, fully explained later on, we will use pointers to a character array to define simple strings, in the following manner:

```c
char * name = "John Smith";
```

This method creates a string which we can only use for reading. If we wish to define a string which can be manipulated, we will need to define it as a local character array:

```c
char name[] = "John Smith";
```

This notation is different because it allocates an array variable so we can manipulate it. The empty brackets notation `[]` tells the compiler to calculate the size of the array automatically. This is in fact the same as allocating it explicitly, adding one to the length of the string:

```c
char name[] = "John Smith";
/* is the same as */
char name[11] = "John Smith";
```

The reason that we need to add one, although the string `John Smith` is exactly 10 characters long, is for the string termination: a special character (equal to 0) which indicates the end of the string. The end of the string is marked because the program does not know the length of the string - only the compiler knows it according to the code.

### String formatting with printf

We can use the `printf` command to format a string together with other strings, in the following manner:

```c
char * name = "John Smith";
int age = 27;

/* prints out 'John Smith is 27 years old.' */
printf("%s is %d years old.\n", name, age);
```

Notice that when printing strings, we must add a newline (`\n`) character so that our next `printf` statement will print in a new line.

### String Length

The function 'strlen' returns the length of the string which has to be passed as an argument:

```c
char * name = "Nikhil";
printf("%d\n",strlen(name));
```

### String comparison

The function `strncmp` compares between two strings, returning the number 0 if they are equal, or a different number if they are different. The arguments are the two strings to be compared, and the maximum comparison length. There is also an unsafe version of this function called `strcmp`, but it is not recommended to use it. For example:

```c
char * name = "John";

if (strncmp(name, "John", 4) == 0) {
    printf("Hello, John!\n");
} else {
    printf("You are not John. Go away.\n");
}
```

### String Concatenation

The function 'strncat' appends first n characters of src string to the destination string where n is min(n,length(src)); The arguments passed are destination string, source string, and n - maximum number of characters to be appended. For Example:

```c
char dest[20]="Hello";
char src[20]="World";
strncat(dest,src,3);
printf("%s\n",dest);
strncat(dest,src,20);
printf("%s\n",dest);
```