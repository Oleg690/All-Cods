function adunarea(){
    let x = document.getElementById('input');
    let y = x.value;
    y = Number(y);
    y++;
    let result = document.getElementById('result');
    result.innerHTML = String(y);
}