
function createTable() {
  // if (!document.getElementById("table1")) {
  var body = document.getElementsByTagName("body")[0]
  var tbl = document.createElement("table");
  tbl.setAttribute("class", "table table-hover table-sm")
  if (!document.getElementById("table1")) {
    var thead = tbl.createTHead();
    var row = thead.insertRow();
    var headers = ["Date", "To-do", "Notes"]
    for (var key of headers) {
      var th = document.createElement("th");
      var text = document.createTextNode(key);
      th.appendChild(text);
      row.appendChild(th);
    }
  }

  var tblBody = document.createElement("tbody");
  for (var i = 0; i < 1; i++) {
    // creates a table row
    var row = document.createElement("tr");

    for (var j = 0; j < 3; j++) {
      // Create a <td> element and a text node, make the text
      // node the contents of the <td>, and put the <td> at
      // the end of the table row
     var cell = document.createElement("td");
      var cellText = document.createTextNode("cell in row "+i+", column "+j);
      cell.appendChild(cellText);
      row.appendChild(cell);
    }

   // add the row to the end of the table body
    tblBody.appendChild(row);
  }

   // put the <tbody> in the <table>
  tbl.appendChild(tblBody);
   // appends <table> into <body>12
  body.appendChild(tbl);
   // sets the border attribute of tbl to 2;
  tbl.setAttribute("border", "2");
  tbl.setAttribute("id", "table1")
}
