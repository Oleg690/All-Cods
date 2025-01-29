cell_1 = document.getElementById('1')
cell_2 = document.getElementById('2')
cell_3 = document.getElementById('3')

let x = 1

function run(){
    if(x == 1){
        noColor()
        cell_2.style.backgroundColor = "yellow";
        x = 2
    }else if(x == 2){
        noColor()
        cell_3.style.backgroundColor = "green";
        x = 3
    }else if(x == 3){
        noColor()
        cell_1.style.backgroundColor = "red";
        x = 1
    }
}

function noColor(){
    cell_1.style.backgroundColor = "white";
    cell_2.style.backgroundColor = "white";
    cell_3.style.backgroundColor = "white";
}