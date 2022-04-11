# Array-Comparison
[[Shell]]
---

Comparison of arrays Shell can handle arrays An array is a variable containing multiple values. Any variable may be used as an array. There is no maximum limit to the size of an array, nor any requirement that member variables be indexed or assigned contiguously. Arrays are zero-based: the first element is indexed with the number 0.

```bash
# basic construct
# array=(value1 value2 ... valueN)
array=(23 45 34 1 2 3)
[[To]] refer to a particular value (e.g. : to refer 3rd value)
echo ${array[2]}

[[To]] refer to all the array values
echo ${array[@]}

[[To]] evaluate the number of elements in an array
echo ${#array[@]}
```