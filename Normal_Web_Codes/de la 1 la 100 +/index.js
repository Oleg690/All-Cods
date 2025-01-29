function run(){
    let i = 0
    let result = 0

    do{
        result += i
        i ++
    }while(i <= 100)

    document.getElementById('1').innerHTML = result
}