pBar = document.querySelector(".progress")

function updateProgressbar(progressBar, value){
    progressBar.querySelector(".progress__fill").style.width = `${value}`;
    progressBar.querySelector(".progress__text").textContent = `${value}`;
}

function runResult(e){
    let result = e.target.response;

    updateProgressbar(pBar, result);
}

function btn1Click(){
    let verify = 'True';

    let oReq = new XMLHttpRequest();

    oReq.onload = runResult;
    let url = 'cgi-bin/main.py?verify=' + verify;

    oReq.open('GET', url);
    oReq.send();
}

window.onload = function(){
    setInterval(() => {
        btn1Click()
    }, 500);
}