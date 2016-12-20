# Pug like language
### just for fun


the block of code below:

```
html
  head
    title my page title
  body
    div(class=block, id=main) this is a div
    input(type=text)
    span I'm a span
    table
      tr 
        td ohh, look, a table 
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
    <div class="block" id="main">
      this is a div
    </div>
    <input type="text"/>
    <span>
      I'm a span
    </span>
    <table>
      <tr>
        <td>
          ohh, look, a table 
        </td>
      </tr>
    </table>
  </body>
</html>

```
