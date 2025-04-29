# jQuery Notes

## To start
Add this at the top of the HTML page. The browser will run any JavaScript inside a `<script>` element. It is important to use `document ready function` because your code may run before your HTML is rendered that would cause bugs.

```
<script>
    $(document).ready(function(){});
</script>
```
## All jQuery functions start with a $, or bling
For example, let's make `button` type-elements bounce. Add a jQuery selector `$("button")` and `.addClass()` function inside the `document ready function`.

```
<script>
  $(document).ready(function() {
    $("button").addClass("animated bounce");   // Added two classes
  });
</script>
```

## Target elements by Class and id
Just like CSS declaractions, type a `.` before the class's name and `#` for id.

```
<script>
  $(document).ready(function() {
    $("button").addClass("animated bounce");
    $(".text-primary").addClass("animated shake")
    $("#target6").addClass("animated fadeOut btn-primary");  // Added three classes
  });
</script>
```
Simiarly, `removeClass()` to remove particular target element and style.

```
<script>
  $(document).ready(function() {
    $("button").addClass("animated bounce");
    $(".well").addClass("animated shake");
    $("#target3").addClass("animated fadeOut");
    $("button").removeClass("btn-default")
  });
</script>
```

## Other functions

- `.html()` to target properties of HTML tags: `$("h3").html("<em>Hello World!</em>")` to change the default `h3` HTML tag.
- `.css()` to overwrite CSS styling rules: `$("#target1").css("background-color", "blue")` to change background color to blue for #target1.
- `.prop()` to access properties of elements: `$("button").prop("disable", true)` to disable button.
- `.remove()` to remove an HTML element: `$("#target4").remove()` to remove #target4 button.
- `.appendTo()` to move an element: `$("#target4").appendTo("#left-well")` to move #target4 from `right-well` to the `left-well`.
- `.clone()` to make copy of that element.
- `.parent()` to access its parent's element: `$("#left-well").parent().css("background-color", "blue")` to access `<div>` and change its background color.
- `.children()` to acess its children's element.
- `.btn:nth-child(n)` to access a specific children: `$(".btn:nth-child(3)").addClass("animated bounce")` to access `.btn` third child.
- `:odd()` and `:even()` to select position. Note that index `0` is odd and `1` is even: `$(".target:odd").addClass("animated shake")` to make #target2 (index 1), #target4 (index 3), and #target6 (index 5) shake.

## Example code

```

<!-- Only change code above this line -->

<div class="container-fluid">
  <h3 class="text-primary text-center">jQuery Playground</h3>
  <div class="row">
    <div class="col-xs-6">
      <h4>#left-well</h4>
      <div class="well" id="left-well">
        <button class="btn btn-default target" id="target1">#target1</button>
        <button class="btn btn-default target" id="target2">#target2</button>
        <button class="btn btn-default target" id="target3">#target3</button>
      </div>
    </div>
    <div class="col-xs-6">
      <h4>#right-well</h4>
      <div class="well" id="right-well">
        <button class="btn btn-default target" id="target4">#target4</button>
        <button class="btn btn-default target" id="target5">#target5</button>
        <button class="btn btn-default target" id="target6">#target6</button>
      </div>
    </div>
  </div>
</div>

```




 
