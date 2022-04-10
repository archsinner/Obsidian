# Lists
[[HTML & CSS]]
---

HTML provides a way to create both an ordered list (with elements counting up, 1, 2, 3...) and an unordered list with bullets instead of numbers. Lists are a good way to formalize a list of items and let the HTML styling do the work for you.

### Ordered lists

Here is an example of how to create an ordered list:

```html
<p>Here is a list of ordered items:</p>
<ol>
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ol>
```

Ordered lists have a "type" attribute which defines the numbering convention to use.

To count using numbers, use type="1":

```html
<p>Here is a list of ordered items:</p>
<ol type="1">
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ol>
```

To count using uppercase letters, use type="A":

```html
<p>Here is a list of ordered items:</p>
<ol type="A">
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ol>
```

To count using lowercase letters, use type="a":

```html
<p>Here is a list of ordered items:</p>
<ol type="a">
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ol>
```

To count using uppercase roman numerals, use type="I":

```html
<p>Here is a list of ordered items:</p>
<ol type="I">
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ol>
```

To count using lowercase roman numerals, use type="i":

```html
<p>Here is a list of ordered items:</p>
<ol type="i">
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ol>
```

### Unordered lists

Here is an example of how to create an unordered list:

Here is a list of unordered items:

  

-   First item
-   Second item
-   Third item

To change the list style attributes, we can use the CSS attribute called `list-style-type`. The available types are:

-   disc
-   circle
-   square
-   none

Here is an example of the disc list style type:

```html
<p>Here is a list of unordered items:</p>    
<ul style="list-style-type: disc">
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ul>
```

Here is an example of the circle list style type:

```html
<p>Here is a list of unordered items:</p>    
<ul style="list-style-type: circle">
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ul>
```

Here is an example of the square list style type:

```html
<p>Here is a list of unordered items:</p>    
<ul style="list-style-type: square">
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ul>
```

Here is an example of the none list style type:

```html
<p>Here is a list of unordered items:</p>    
<ul style="list-style-type: none">
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ul>
```