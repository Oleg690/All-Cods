function runResult(e){
    let result = e.target.response;
    
    document.getElementById('4').innerHTML = 'Result: ' + result;
}

function btn1Click(){
    let x = document.getElementById('1').value;

    let oReq = new XMLHttpRequest();

    oReq.onload = runResult;
    let url = '/cgi-bin/verifyIP.py?x=' + x;

    oReq.open('GET', url);
    oReq.send();
}