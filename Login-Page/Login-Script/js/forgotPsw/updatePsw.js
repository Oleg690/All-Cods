// Paragraph to show error
let error = document.querySelector("#errorForNewPassword");

// Eye to see or hide the password
let eye1 = document.getElementById("seePassword1");
let eye2 = document.getElementById("seePassword2");

// Password inputs for update pass
let passwInput1 = document.getElementById("password");
let passwInput2 = document.getElementById("confirmPsw");

// Functions: ↓

function runResult(e) {
  result = e.target.response;

  let firstSpaceIndex = result.indexOf(" ");

  let verifyer = result.slice(0, firstSpaceIndex);
  let errorToAlert = result.slice(firstSpaceIndex + 1);

  if (verifyer == "True") {
    error.style.color = "rgb(0, 255, 0)";
    error.innerHTML = "Password Updated!";
    error.style.transform = "translate(5px, 40px)";
    localStorage.removeItem("email");
    setTimeout(function () {
      window.location.href = "../../Web-Pages/authentification.html";
    }, 2000);
  } else {
    error.style.color = "rgb(255, 0, 0)";
    error.innerHTML = errorToAlert;
    error.style.transform = "translate(5px, 40px)";
  }
}

function updatePsw() {
  let password = document.getElementById("password").value;
  let confirmPassword = document.getElementById("confirmPsw").value;
  let email = localStorage.getItem("email");

  let url =
    "../../cgi-bin/verify/updatePsw/changePsw.py?password=" +
    password +
    "&confirmPsw=" +
    confirmPassword +
    "&email=" +
    email;

  sendAll(url);
}

eye1.addEventListener("click", function () {
  seePass(passwInput1, eye1);
});

eye2.addEventListener("click", function () {
  seePass(passwInput2, eye2);
});

function seePass(passwInput, eye) {
  if (passwInput.type == "password") {
    passwInput.type = "text";
    eye.src = "../../img/eye-open.png";
  } else {
    passwInput.type = "password";
    eye.src = "../../img/eye-close.png";
  }
}

function sendAll(url) {
  let oReq = new XMLHttpRequest();
  oReq.onload = runResult;
  oReq.open("GET", url);
  oReq.send();
}
