// To detect where on page we are, on login side or register

let formVerifyer = "login";

// For user and email from login

let input1 = document.querySelector("#user");
let email = document.getElementById("email");

// For user and email from register

let input3 = document.querySelector("#user-register");
let emailRegister = document.getElementById("email-register");

// For Password input-login

error = document.getElementById("error");
seePsw = document.querySelector("#seePassword");
passwInput = document.getElementById("password");

// For register inputs

seePsw1 = document.querySelector("#seePassword1-register");
passwInput1 = document.getElementById("password-register");

seePsw2 = document.querySelector("#seePassword2-register");
passwInput2 = document.getElementById("verifyPass-register");

// For register error

error2 = document.getElementById("error2");
error3 = document.getElementById("error3");

// Buttons for changing betwen login and register form

const moveRegister = document.getElementById("moveRegister");
const registerForm = document.getElementById("registerForm");

const moveLogin = document.getElementById("moveLogin");
const loginForm = document.getElementById("loginForm");

// The form for all the login and register elements

wrapper = document.querySelector(".wrapper");

// Event Listners for muving the forms

moveLogin.addEventListener("click", () => {
  formVerifyer = "login";
  registerForm.style.transform = "translateX(440px)";
  loginForm.style.transform = "translateX(0px)";
  reset();
});

moveRegister.addEventListener("click", () => {
  formVerifyer = "register";
  registerForm.style.transform = "translateX(0px)";
  loginForm.style.transform = "translateX(-440px)";
  reset();
});

function reset() {
  input1.value = "";
  input3.value = "";
  emailRegister.value = "";
  passwInput.value = "";
  passwInput1.value = "";
  passwInput2.value = "";
  error.style.transform = "translate(5px, 170px)";
  error2.style.transform = "translate(-5px, 155px)";
  error3.style.transform = "translate(-5px, 155px)";
  passwInput.type = "password";
  seePsw.src = "../img/eye-close.png";
  passwInput1.type = "password";
  seePsw1.src = "../img/eye-close.png";
  passwInput2.type = "password";
  seePsw2.src = "../img/eye-close.png";
}

function runResult(e) {
  let result = e.target.response;

  result = result.trim();

  let firstSpaceIndex = result.indexOf(" ");

  let verifyer = result.slice(0, firstSpaceIndex);
  let errorToAlert = result.slice(firstSpaceIndex + 1);

  let userToSend = document.getElementById("user").value;

  if (formVerifyer == "login") {
    if (verifyer == "truelogin") {
      error.style.transform = "translate(5px, 170px)";

      localStorage.setItem("mainVerify", "True");
      localStorage.setItem("user", userToSend);
      window.location.href = "../index.html";
    } else {
      error.innerHTML = errorToAlert;
      error.style.transform = "translate(5px, 100px)";
    }
  } else {
    if (verifyer == "trueregister") {
      error3.style.transform = "translate(-5px, 90px)";
      error2.style.transform = "translate(-5px, 155px)";
    } else {
      error2.style.transform = "translate(-5px, 90px)";
      error3.style.transform = "translate(-5px, 155px)";
      error2.innerHTML = errorToAlert;
    }
  }
}

function btn1Click() {
  let user = document.getElementById("user").value;
  let password = document.getElementById("password").value;

  let url = "../cgi-bin/verify/login.py?user=" + user + "&password=" + password;

  getRequestSend(url);
}

function btn2Click() {
  let user = document.getElementById("user-register").value;
  let email = document.getElementById("email-register").value;
  let password = document.getElementById("password-register").value;
  let verifyPassword = document.getElementById("verifyPass-register").value;

  let url =
    "../cgi-bin/verify/register.py?user=" +
    user +
    "&email=" +
    email +
    "&password=" +
    password +
    "&confirmPass=" +
    verifyPassword;

  getRequestSend(url);
}

seePsw.addEventListener("click", function () {
  seePassword(passwInput, seePsw);
});

seePsw1.addEventListener("click", function () {
  seePassword(passwInput1, seePsw1);
});

seePsw2.addEventListener("click", function () {
  seePassword(passwInput2, seePsw2);
});

function seePassword(passInput, passEye) {
  if (passInput.type == "password") {
    passInput.type = "text";
    passEye.src = "../img/eye-open.png";
  } else {
    passInput.type = "password";
    passEye.src = "../img/eye-close.png";
  }
}

function getRequestSend(url) {
  let oReq = new XMLHttpRequest();
  oReq.open("GET", url);
  oReq.send();
  oReq.onload = runResult;
}

window.addEventListener("resize", function () {
  var windowHeight =
    window.innerHeight ||
    document.documentElement.clientHeight ||
    document.body.clientHeight;
  var windowWidth =
    window.innerWidth ||
    document.documentElement.clientWidth ||
    document.body.clientWidth;

  if (windowHeight > 864) {
    wrapper.style.transform = "translate(-50%, -50%) scale(1.5)";
  } else if (windowWidth < 600) {
    wrapper.style.transform = "translate(-50%, -50%) scale(0.7)";
  } else {
    wrapper.style.transform = "translate(-50%, -50%) scale(1)";
  }
});

window.onload = function () {
  localStorage.removeItem("mainVerify");
};
