# Box Sizing
[[HTML & CSS]]
---

Without any alterations, the size of a box is calcualted like this: width + padding + border = actual width of an element height + padding + border = actual height of an element

So when you set the size of an element, the image will often appear bigger, because the new sizings are added to the original. However, the element with the same sizing can appear differnet because of different paddings added to each element. The property allows the padding and border to be included in the element's total width and height. The allows the padding and border to be included in an element.

```html
<!DOCTYPE html>
<html>
<head>
    <style>
    <box-sizing: border-box;>
    </style>
</head>
<body>
</body>
</html>
```

To include the border you need to include the border code; border: size type color;

```html
<!DOCTYPE html>
<html>
<head>
    <style>
    <border: 1px solid blue>
    <box-sizing: border-box;>
    </style>
</head>
<body>
</body>
</html>
```