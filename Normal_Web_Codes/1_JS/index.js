function run(){
        
    x = Number(document.getElementById("1").value)

    result = ''

    i = 1

    while(i <= x){
        result += String(i) + "<br>"

        i++
    }

    result += "Am invatat a numara"

    document.getElementById("2").innerHTML = result
}