let user = "";
let email = "";

profilePic = document.getElementById("profilePic");
logOut = document.getElementById("logOut");

window.onload = function () {
  const mainVerify = localStorage.getItem("mainVerify");
  const user = localStorage.getItem("user");

  getAllInformation(user);

  if (mainVerify != "True") {
    window.location.href = "../Web-Pages/authentification.html";
  }
};

function getAllInformation() {
  const information = localStorage.getItem("user");

  if (information.includes("@")) {
    let url = "../cgi-bin/getInformation/fromEmail.py?email=" + information;
    sendToScript(url);
  } else {
    let url = "../cgi-bin/getInformation/fromUser.py?user=" + information;
    sendToScript(url);
  }
}

function sendToScript(url) {
  let oReq = new XMLHttpRequest();

  oReq.onload = runResult2;
  oReq.open("GET", url);
  oReq.send();
}

function runResult2(e) {
  let result = e.target.response;

  result = JSON.parse(result);

  user = result[0][1];
  email = result[0][2];

  localStorage.setItem("userForSettings", user);
  localStorage.setItem("emailForSettings", email);

  getImgUrl(user);
}

function getImgUrl(user) {
  let oReq = new XMLHttpRequest();

  oReq.onload = runResult1;
  let url = "../cgi-bin/getInformation/imgReq/imgSel.py?user=" + user;

  oReq.open("GET", url);
  oReq.send();
}

function runResult1(e) {
  let result = e.target.response;

  result = JSON.parse(result);

  if (result == "none" || result == null) {
    profilePic.src = "../img/accountImg/profile.png";
  } else {
    profilePic.src = result;
  }
}

profilePic.addEventListener("click", function () {
  window.location.href = "../Web-Pages/settings.html";
});

logOut.addEventListener("click", function () {
  localStorage.removeItem("userForSettings");
  localStorage.removeItem("emailForSettings");

  localStorage.setItem("mainVerify", "False");
  window.location.href = "../Web-Pages/authentification.html";
});







