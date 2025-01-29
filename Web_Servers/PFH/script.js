player_1 = document.getElementById('1');
player_2 = document.getElementById('2');

result_btn = document.getElementById('result');

function run(){
    x = player_1.value;
    y = player_2.value;
    verify()
    result()
}

function verify(){
    if(x == 'Piatră' && y == 'Foarfece'){
        resultText = 'Player 1 Won!'
    }else if(x == 'Foarfece' && y == 'Hârtie'){
        resultText = 'Player 1 Won!'
    }else if(x == 'Hârtie' && y == 'Piatră'){
        resultText = 'Player 1 Won!'
    }else if(x == y){
        resultText = 'Equal!'
    }else{
        resultText = 'Player 2 Won!'
    }
}

function result(){
    result_btn.innerHTML = resultText;
}