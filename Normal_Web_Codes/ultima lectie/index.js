function run(){
    let psw1 = ''
    let psw2 = ''

    do{
        psw1 = prompt("intoduceti parola")
        psw2 = prompt("intoduceti parola din nou")
    }while(psw1 != psw2)

    alert("Parola a fost setata")
}