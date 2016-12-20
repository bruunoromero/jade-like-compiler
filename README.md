# Pug like language
### just for fun


the block of code above:

```
html
  head
    title teste
  body
    div(class=main) testando aqui meu compilador
    input(type=text)
    span teste
    table
      tr
        td mais um teste aqui
```

becomes this:
```html
<html>
  <head>
    <title>
      teste
    </title>
  </head>
  <body>
    <div class="main">
      testando aqui meu compilador
    </div>
    <input type="text"  />
    <span>
      teste
    </span>
    <table>
      <tr>
        <td>
          mais um teste aqui
        </td>
      </tr>
    </table>
  </body>
</html>
```