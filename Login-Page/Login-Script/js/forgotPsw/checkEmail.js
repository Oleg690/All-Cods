let result = "";

// The error

let paragraph = document.getElementById("error");

// Paragraph to show error or send code

let sendError = document.querySelector("#sendError");
let emailSend = document.querySelector("#emailSend");

// Wrapper for the email sender

let sendEmail = document.querySelector("#sendEmail");

// Button for the sender

let checkCodeDiv = document.querySelector("#checkCode");

// For wrong code, it pops out

let checkErrorPar = document.getElementById("checkErrorPar");

// If wrong email, the link to go back

let backToEmail = document.querySelector(".backToEmail");

// Info needed to pass the path

let email = document.querySelector("#email");
let imputCode = document.getElementById("code");

function containsNumbers(inputString) {
  var regex = /\d/;

  return regex.test(inputString);
}

function runResult(e) {
  result = e.target.response;

  if (containsNumbers(result) == false) {
    sendError.innerHTML = result;
    sendError.style.transform = "translate(5px, 60px)";
  } else {
    sendError.style.transform = "translate(5px, 120px)";
    sendEmail.style.transform = "translateX(-500px)";
    checkCodeDiv.style.transform = "translateX(0px)";
  }
}

function sendCode() {
  let email = document.getElementById("email").value;
  localStorage.setItem("email", email);

  let url = "../../cgi-bin/verify/emailSender/emailSender.py?email=" + email;

  sendUrl(url)
}

function checkCode() {
  let imputCode = document.querySelector("#code").value;

  if (parseInt(result) === parseInt(imputCode)) {
    checkErrorPar.style.transform = "translate(5px, 120px)";
    window.location.href = "../../Web-Pages/forgotPsw/updatePsw.html";
  } else {
    checkErrorPar.style.transform = "translate(5px, 60px)";
  }
}

function reset() {
  imputCode.value = "";
  email.value = "";
}

backToEmail.addEventListener("click", () => {
  sendEmail.style.transform = "translateX(0px)";
  checkCodeDiv.style.transform = "translateX(500px)";
  reset();
});

function sendUrl(url){
  let oReq = new XMLHttpRequest();
  oReq.onload = runResult;
  oReq.open("GET", url);
  oReq.send();
}