let numarul = document.getElementById('1');
let result_tag = document.getElementById('result');
let mounth = '';

function get_mounth(){
    x = numarul.value;
    x = Number(x);
    if(x >= 6 && x <= 8){
        mounth = 'Vara'
        result()
    }else if(x >= 9 && x <= 11) {
        mounth = 'Toamna'
        result()
    }
    else if(x == 12 || x == 1 || x == 2) {
        mounth = 'Iarna'
        result()
    }
    else if(x >= 3 && x <= 5) {
        mounth = 'Primăvara'
        result()
    }else{
        mounth = 'Nu am găsit lună cu numărul ' + x
        result()
    }
}

function result(){
    result_tag.innerHTML = mounth;
}