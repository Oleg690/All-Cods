let profilePic = document.getElementById("profile-pic");
let inputFile = document.getElementById("input-file");

let errorPopup = document.getElementById("error");

const tabBtn = document.querySelectorAll(".tab");
const tab = document.querySelectorAll(".tabshow");

function tabs(panelIndex) {
  tab.forEach(function (node) {
    node.style.display = "none";
  });
  tab[panelIndex].style.display = "block";
}

const firstTab = document.getElementById("1");
const secondTab = document.getElementById("2");

firstTab.addEventListener("click", function () {
  resetPopup()
  firstTab.classList.add("active");
  secondTab.classList.remove("active");
});

secondTab.addEventListener("click", function () {
  resetPopup()
  secondTab.classList.add("active");
  firstTab.classList.remove("active");
});

tabs(0);

window.onload = function () {
  infoGetter();
};

function infoGetter() {
  let user = localStorage.getItem("userForSettings");
  let email = localStorage.getItem("emailForSettings");
  getPassword(user, email);

  document.getElementById("userInfo").value = user;
  document.getElementById("emailInfo").value = email;

  getImgUrl(user);
}

function getImgUrl(user) {
  let oReq = new XMLHttpRequest();

  oReq.onerror = function () {
    alert("Request failed");
  };

  let url = "../cgi-bin/getInformation/imgReq/imgSel.py?user=" + user;

  oReq.open("GET", url);
  oReq.send();

  oReq.onload = runResult2;
}

function runResult2(e) {
  let result = e.target.response;

  result = JSON.parse(result);

  if (result == "none" || result == null) {
    profilePic.src = "../img/accountImg/profile.png";
  } else {
    profilePic.src = result;
  }
}

let popup = document.getElementById("popup");

function verifyIfDelOrUpdate(verify) {
  localStorage.setItem('verificator', verify);
  errorPopup.style.top = "-55px";
  popup.style.top = "40px";
}

function findBtnToExecute(verify) {
  let info = localStorage.getItem('verificator');
  if (info == "update") {
    updateAccount(verify);
  } else if (info == "delete") {
    deleteAccount(verify);
  }
  localStorage.removeItem('verificator')
}

function deleteAccount(verify) {
  errorPopup.style.top = "-55px";
  if (verify == "yes") {
    const user = localStorage.getItem("userForSettings");
    const email = localStorage.getItem("emailForSettings");

    let url =
      "../cgi-bin/getInformation/deleteAccount/delete.py?user=" +
      user +
      "&email=" +
      email;

    sendToScript(url);

    localStorage.setItem("mainVerify", "False");
    localStorage.removeItem("userForSettings");
    localStorage.removeItem("emailForSettings");

    window.location.href = "../index.html";
  } else {
    popup.style.top = "-55px";
  }
}

function updateAccount(verify) {
  errorPopup.style.top = "-55px";
  if (verify == "yes") {
    let user = document.getElementById("userUpdate").value;
    let email = document.getElementById("emailUpdate").value;
    let password = document.getElementById("passwordUpdate").value;

    const userCurrent = localStorage.getItem("userForSettings");
    const emailCurrent = localStorage.getItem("emailForSettings");

    let url =
      "../cgi-bin/updateInfo/updateDatabase.py?user=" +
      user +
      "&email=" +
      email +
      "&password=" +
      password +
      "&userCurrent=" +
      userCurrent +
      "&emailCurrent=" +
      emailCurrent;

    sendToScriptUpdate(url);
  } else {
    popup.style.top = "-55px";
  }
}

function sendToScript(url) {
  let oReq = new XMLHttpRequest();

  oReq.open("GET", url);
  oReq.send();
}

function sendToScriptUpdate(url) {
  let oReq = new XMLHttpRequest();

  oReq.onload = showUpdate;

  oReq.open("GET", url);
  oReq.send();
}

function showUpdate(e) {
  result = e.target.response;
  result = JSON.parse(result);

  let resultLength = result.length;

  if (resultLength == 2) {
    localStorage.setItem("userForSettings", result[0]);
    localStorage.setItem("emailForSettings", result[1]);
    console.log(result);
    infoGetter();
    resetUpdateInfo();
    resetPopup();
  } else if (resultLength == 1) {
    console.log(result);
    document.getElementById("ParError").innerHTML = result[0];
    errorPopup.style.top = "40px";
    popup.style.top = "-55px";

    setTimeout(() => {
      errorPopup.style.top = "-55px";
    }, 5000);
  }
}

function resetUpdateInfo() {
  document.getElementById("userUpdate").value = "";
  document.getElementById("emailUpdate").value = "";
  document.getElementById("passwordUpdate").value = "";
}

function resetPopup() {
  popup.style.top = "-55px";
  errorPopup.style.top = "-55px";
}

inputFile.addEventListener("change", () => {
  const fr = new FileReader();

  fr.readAsDataURL(inputFile.files[0]);

  fr.addEventListener("load", () => {
    const urlImg = fr.result;

    sendPostRequest(urlImg);
  });
});

function sendPostRequest(dataInput) {
  user = localStorage.getItem("userForSettings");
  var xhr = new XMLHttpRequest();

  xhr.open("POST", "../cgi-bin/getInformation/imgReq/imgUpd.py", true);
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      getImgUrl(user);
    }
  };

  var data =
    "user=" +
    encodeURIComponent(user) +
    "&dataInput=" +
    encodeURIComponent(dataInput);

  xhr.send(data);
}

function getPassword(user, email) {
  let url =
    "../cgi-bin/getInformation/getPassword/getPassword.py?user=" +
    user +
    "&email=" +
    email;
  getPasswordSend(url);
}

function getPasswordSend(url) {
  let oReq = new XMLHttpRequest();

  oReq.open("GET", url);
  oReq.send();

  oReq.onload = readPassword;
}

function readPassword(e) {
  result = e.target.response;

  result = JSON.parse(result);

  document.getElementById("passwordInfo").value = result;
}

let eye = document.getElementById("eye");
let seePassword = document.getElementById("passwordUpdate");

eye.addEventListener("click", function () {
  if (seePassword.type == "password") {
    seePassword.type = "text";
    eye.src = "../img/eye-open.png";
  } else {
    seePassword.type = "password";
    eye.src = "../img/eye-close.png";
  }
});
