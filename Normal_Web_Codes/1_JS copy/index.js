function run(){
        
    x = Number(document.getElementById("1").value)

    result = ''

    i = 0

    while(x >= i){
        result += String(x) + "<br>"
        x = x - 1
    }

    result += "Start"

    document.getElementById("2").innerHTML = result
}