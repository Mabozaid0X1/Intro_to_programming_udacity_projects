      // Select color input
     //Select size input
    //I can also use "querySelector" instead of "getElementById", but I will add #

     var canvas = document.getElementById('pixelCanvas');
   var gridHeight = document.getElementById('inputHeight');
   var gridWidth = document.getElementById('inputWidth');
   var form = document.getElementById('sizePicker');
   var clickFunction = function(event) {
         event.preventDefault();
    makeGrid();
    };
    // When size is submitted by the user, call makeGrid()

      var myFunction = function (event) {
    const color = document.getElementById('colorPicker');
    event.target.style.backgroundColor = color.value;
    }
      function makeGrid() {
    //Your code goes here!
    canvas.innerHTML = '';

    for (let i = 0; i < gridHeight.value; i++) {
      const myTr = document.createElement('tr');
      canvas.appendChild(myTr)

       for (let j = 0; j < gridWidth.value; j++) {
      const myTd = document.createElement('td');
      myTr.appendChild(myTd);
      myTd.addEventListener('click' , myFunction)
        }
      }
    }
    form.addEventListener('submit', clickFunction);
    //I searched a lot to make this code on (w3school,MDN,Jquery) and I ask some frieds on slack;
