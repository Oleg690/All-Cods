function runResult(e){
    let result = e.target.response;

    document.getElementById('4').innerHTML = 'Result: ' + result;
}

function btn1Click(){
    let x = document.getElementById('1').value;
    let y = document.getElementById('2').value;

    let operation = document.getElementById('3').value;

    let oReq = new XMLHttpRequest();

    oReq.onload = runResult;
    let url = '/cgi-bin/run.py?x=' + x + '&y='+ y + '&operation=' + operation;

    oReq.open('GET', url);
    oReq.send();
}