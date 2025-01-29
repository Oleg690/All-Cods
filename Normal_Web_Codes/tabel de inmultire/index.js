function run(){
        
    x = Number(document.getElementById("1").value)

    result = ''

    y = 1

    z = x*y

    while(y <= 10){
        z = x*y
        result += x + ' ' + 'x' + ' ' + y + ' ' + '=' + ' ' + z + "<br>"
        y += 1
    }

    result += "Tabla inmultirii cu " + x

    document.getElementById("2").innerHTML = result
}