let primul_numar = document.getElementById('1');
let al_doilea_numar = document.getElementById('2');
let result = document.getElementById('result');

function get_numbers(){
    x = primul_numar.value;
    y = al_doilea_numar.value;
    x = Number(x);
    y = Number(y);
}

function aduna(){
    get_numbers()
    z = x + y;
    result.innerHTML = 'Result: ' + String(x) + ' + ' + String(y)+ ' = ' + String(z);
}

function scade(){
    get_numbers()
    z = x - y;
    result.innerHTML = 'Result: ' + String(x) + ' - ' + String(y)+ ' = ' + String(z);
}

function inmulteste(){
    get_numbers()
    z = x * y;
    result.innerHTML = 'Result: ' + String(x) + ' × ' + String(y)+ ' = ' + String(z);
}

function imparteste(){
    get_numbers()
    z = x / y;
    result.innerHTML = 'Result: ' + String(x) + ' : ' + String(y)+ ' = ' + String(z);
}