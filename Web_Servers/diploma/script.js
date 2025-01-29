//List with items in the cart
let checkedList = [];

//Add

let nameAdd = document.getElementById("nameAdd");
let priceAdd = document.getElementById("priceAdd");

//Del

let idDel = document.getElementById("idDel");

//Update

let idUpdate = document.getElementById("idUpdate");
let nameUpdate = document.getElementById("nameUpdate");
let priceUpdate = document.getElementById("priceUpdate");

//----------------------------------------------------------

window.onload = run();

function runResult(e) {
  let result = e.target.response;

  result = JSON.parse(result);

  document.getElementById("table").innerHTML = result;

  counterResult();
}

function run() {
  execGetQuery("cgi-bin/getgoods.py");
}

function add() {
  let name = document.getElementById("nameAdd").value;
  let price = document.getElementById("priceAdd").value;

  let url = "cgi-bin/functions/add.py?name=" + name + "&price=" + price;

  execGetQuery(url);

  resetValues();
}

function del() {
  let id = document.getElementById("idDel").value;

  let url = "cgi-bin/functions/delete.py?id=" + id;

  execGetQuery(url);

  resetValues();
}

function update() {
  let id = document.getElementById("idUpdate").value;
  let name = document.getElementById("nameUpdate").value;
  let price = document.getElementById("priceUpdate").value;

  let url =
    "cgi-bin/functions/update.py?id=" +
    id +
    "&name=" +
    name +
    "&price=" +
    price;

  execGetQuery(url);

  resetValues();
}

function execGetQuery(url) {
  let oReq = new XMLHttpRequest();
  oReq.open("GET", url);
  oReq.send();
  oReq.onload = runResult;
}

function delBtn() {
  let url = "cgi-bin/dropTable.py";
  execGetQuery(url);
}

function counterResult() {
  let url = "cgi-bin/counter.py";

  let oReq = new XMLHttpRequest();
  oReq.open("GET", url);
  oReq.send();
  oReq.onload = counterShow;
}

function counterShow(e) {
  result = e.target.response;

  document.getElementById(
    "items"
  ).innerHTML = `Items in the database: ${result}`;
}

function resetValues() {
  nameAdd.value = "";
  priceAdd.value = "";

  idDel.value = "";

  idUpdate.value = "";
  nameUpdate.value = "";
  priceUpdate.value = "";
}

function infoBtn(info, verify) {
  let url =
    "cgi-bin/getInformations/infoGeter.py?info=" + info + "&verify=" + verify;

  execGetInfo(url);
}

function execGetInfo(url) {
  let oReq = new XMLHttpRequest();
  oReq.open("GET", url);
  oReq.send();
  oReq.onload = runResultShowInfo;
}

function runResultShowInfo(e) {
  result = e.target.response;

  result = JSON.parse(result);

  document.getElementById("result").innerHTML = result;
}

/*function check_box_click(item) {--> functia cu parametrul item
  if (item.checked == true) {--> vedem daca checkBox-ul este on or off, daca e on, inram in if
    checkedList.push(item.id); --> adaugam in lista checkedList id la item-ul cu butonul on
  } else {--> daca checkBox-ul este off, intram in else 
    let idexOfItem = checkedList.indexOf(item.id);--> gasim idex-ul la checkBox-ul care lam pus pe off
    checkedList.splice(idexOfItem, 1);--> scoatem acel index din lista
  }
  console.log(checkedList);--> aratam lista in consola
}*/
//   Comentariile pentru functia de mai jos
//                 ↓

function check_box_click(item) {
  if (item.checked == true) {
    checkedList.push(item.id);
  } else {
    let indexOfItem = checkedList.indexOf(item.id);
    checkedList.splice(indexOfItem, 1);
  }
  //console.log(checkedList);
}

function toCart() {
  if (checkedList.length == 0) {
    alert('Alegeti niste lucruri ca sa le cumparati!')
  } else {
    window.open(
      "/cgi-bin/CartList/cart.py?goods=" + JSON.stringify(checkedList)
    );
  }
}
