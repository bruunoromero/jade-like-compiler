# Pug like language
### just for fun


the block of code above:

```
html
  head
    title my page title
  body
    div(class=main) this is a div
    input(type=text)
    span I'm a span
    table
      tr
        ohh, look, a table 
```

becomes this:
```html
<html>
  <head>
    <title>
      my page title
    </title>
  </head>
  <body>
    <div class="main">
      this is a div
    </div>
    <input type="text"  />
    <span>
      I'm a span
    </span>
    <table>
      <tr>
        ohh, look, a table 
      </tr>
    </table>
  </body>
</html>
```