function run(){

    result = ''

    y = 1

    for(let y = 1; y <= 10; y++){
        for(let x = 1; x <= 10; x++){
        z = x*y
        result += x + ' ' + 'x' + ' ' + y + ' ' + '=' + ' ' + z + "<br>"

        if(x >= 10){
                result += "Tabla inmultirii cu " + y + '<br>'
            }
    }
    }
    
    document.getElementById("1").innerHTML = result 
}