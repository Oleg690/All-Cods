button = document.getElementById('button');
select = document.getElementById('select');
result = document.getElementById('result');

function run(){
    x = select.value;
    if(x == 'EN'){
        inceput = 'The language was set to: ';
        result_btn()
    }else if(x == 'RO'){
        inceput = 'Limba a fost setată la: ';
        result_btn()
    }else if(x == 'RU'){
        inceput = 'Язык был установлен на: ';
        result_btn()
    }
}

function result_btn(){
    result.innerHTML = inceput + String(x);
}
