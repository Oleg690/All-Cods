tabel = document.getElementById('4');

function runResult(e){
    let result = e.target.response;
    
    tabel.innerHTML = '<table border="1px" id="4">' + result + '</table>';
}

function btn1Click(){
    let x = document.getElementById('1').value;

    let oReq = new XMLHttpRequest();

    oReq.onload = runResult;
    let url = '/cgi-bin/tableSize.py?x=' + x;

    oReq.open('GET', url);
    oReq.send();
}