function run(){
        
    x = Number(document.getElementById("1").value)

    result = ''

    rest = ''

    if(x < 40){
        money += x
        result += "Nu va ajung bani, mai trebuie sa puneti"
    }
    else if(x >= 40){
        rest = x - 40
        result += "Cafeaua este gata. Restul dmv este: " + rest + ' lei'
    }

    document.getElementById("2").innerHTML = result
}