# Loops
[[Shell]]
---

### bash for loop

```bash
# basic construct
for arg in [list]
do
 command(s)...
done
```

For each pass through the loop, arg takes on the value of each successive value in the list. Then the command(s) are executed.

```bash
# loop on array member
NAMES=(Joe Jenny Sara Tony)
for N in ${NAMES[@]} ; do
  echo "My name is $N"
done

# loop on command output results
for f in $( ls prog.sh /etc/localtime ) ; do
  echo "File is: $f"
done
```

### bash while loop

```bash
# basic construct
while [ condition ]
do
 command(s)...
done
```

The while construct tests for a condition, and if true, executes commands. It keeps looping as long as the condition is true.

```bash
COUNT=4
while [ $COUNT -gt 0 ]; do
  echo "Value of count is: $COUNT"
  COUNT=$(($COUNT - 1))
done
```

### bash until loop

```bash
# basic construct
until [ condition ]
do
 command(s)...
done
```

The until construct tests for a condition, and if false, executes commands. It keeps looping as long as the condition is false (opposite of while construct)

```bash
COUNT=1
until [ $COUNT -gt 5 ]; do
  echo "Value of count is: $COUNT"
  COUNT=$(($COUNT + 1))
done
```

### "break" and "continue" statements

break and continue can be used to control the loop execution of for, while and until constructs. continue is used to skip the rest of a particular loop iteration, whereas break is used to skip the entire rest of loop. A few examples:

```bash
# Prints out 0,1,2,3,4

COUNT=0
while [ $COUNT -ge 0 ]; do
  echo "Value of COUNT is: $COUNT"
  COUNT=$((COUNT+1))
  if [ $COUNT -ge 5 ] ; then
    break
  fi
done

# Prints out only odd numbers - 1,3,5,7,9
COUNT=0
while [ $COUNT -lt 10 ]; do
  COUNT=$((COUNT+1))
  # Check if COUNT is even
  if [ $(($COUNT % 2)) = 0 ] ; then
    continue
  fi
  echo $COUNT
done
```