function run(){
    let x = document.getElementById("1").getContext("2d")

    for(let y = 100; y <= 300; y = y + 50){
        
        x.moveTo(50, y)
        x.lineTo(300, y)

        x.stroke()
    }
}