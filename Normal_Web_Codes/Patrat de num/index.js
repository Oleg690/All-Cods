function run(){

    let x = Number(document.getElementById('1').value);

    let result = '';

    for(let i = 0; i < x; i++)
    {
        for(let j = 0; j < x; j++){
            result += '* ';
        }
        result += '<br>';
    }
    
    document.getElementById("2").innerHTML = result 
}
