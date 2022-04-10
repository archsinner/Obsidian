# Input Pseudo-classes
[[HTML & CSS]]
---

There are several pseudo-classes aimed to style HTML forms according to their configuration.

### Checked

The CSS :active pseudo-class defines the styles to use for a checkbox element in a checked state

```html
<style>
input:checked {
    margin-left: 50px;
}
</style>
<form>
    <p><input type="checkbox"> First Option</p>
    <p><input type="checkbox"> Second Option</p>
    <p><input type="checkbox"> Third Option</p>        
</form>
```

### Enabled & Disabled Form Inputs

The CSS :enabled and :disabled pseudo-class defines the styles to use according to whether or not a form input field is enabled or disabled.

```html
<style>
input:disabled {
    color: gray;    
}

input:enabled {
    font-weight: bold;    
}
</style>
<form>
    <p><input type="text" value="First Option"></p>
    <p><input type="text" value="Second Option"></p>
    <p><input type="text" value="Third Option"></p>        
</form>
```

### Optional and required

### Read-only and read-write

### Valid and invalid

### In-range and out-of-range