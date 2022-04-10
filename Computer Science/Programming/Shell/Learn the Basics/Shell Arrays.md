# Arrays
[[Shell]]
---

An array can hold several values under one name. Array naming is the same as variables naming. An array is initialized by assign space-delimited values enclosed in ()

```bash
my_array=(apple banana "Fruit Basket" orange)
new_array[2]=apricot
```

Array members need not be consecutive or contiguous. Some members of the array can be left uninitialized.

The total number of elements in the array is referenced by ${#arrayname[@]}

```bash
my_array=(apple banana "Fruit Basket" orange)
echo  ${#my_array[@]}                   # 4
```

The array elements can be accessed with their numeric index. The index of the first element is 0.

```bash
my_array=(apple banana "Fruit Basket" orange)
echo ${my_array[3]}                     # orange - note that curly brackets are needed
# adding another array element
my_array[4]="carrot"                    # value assignment without a $ and curly brackets
echo ${#my_array[@]}                    # 5
echo ${my_array[${#my_array[@]}-1]}     # carrot
```