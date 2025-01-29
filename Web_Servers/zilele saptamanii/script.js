let numarul = document.getElementById('1');
let result_tag = document.getElementById('result');
let day = '';

function get_day(){
    x = numarul.value;
    x = Number(x);
    if(x == 1){
        day = 'Luni'
        result()
    }else if(x == 2) {
        day = 'Marți'
        console.log(day)
        result()
    }
    else if(x == '3') {
        day = 'Miercuri'
        result()
    }
    else if(x == 4) {
        day = 'Joi'
        result()
    }
    else if(x == 5) {
        day = 'Vineri'
        result()
    }
    else if(x == 6) {
        day = 'Sâmbătă'
        result()
    }
    else if(x == 7) {
        day = 'Duminică'
        result()
    }else{
        day = 'Nu am găsit zi cu numărul ' + x
        result()
    }
}

function result(){
    result_tag.innerHTML = day;
}