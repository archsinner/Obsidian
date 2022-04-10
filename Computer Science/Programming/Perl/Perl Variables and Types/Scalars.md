# Scalars

---

A Perl scalar variable holds a single string or numeric value. Perl supports many operators on scalars:

-   Concatenation of string values via the `.` (dot) operator.
-   Math functions on numeric values: `+ - * / % ^^` as well as a rich set of functions.
-   Operations on own variable: `+= -= .= ++ --` etc.

Some examples:

```perl
# scalar variable example
$item_name = "Apple";
$item_price = 13.50;
$item_count = 5;
print "The total for $item_count $item_name" . "s" . " will be: " . $item_count * $item_price . " Dollars.\n";
# or alternately
$total = $item_count * $item_price;
$item_name_plural = $item_name . "s";
print "The total for $item_count $item_name_plural will be: $total Dollars.\n";
```

## Exercise

The Boeing 747-8 is a wide-body jet airliner developed by Boeing Commercial Airplanes. It is 250 feet long, it weighs 987,392 Pounds and costs 357.5 Million US Dollars. A person in Europe asks you to convert the length to meters, the weight to kilograms and the cost to euros.

Use the conversion variable values to print 3 lines:

The jet is **_**_ Meters long.

The jet weighs **_**_ Kilograms.

The jet costs **_**_ Million Euro.