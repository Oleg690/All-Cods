function run(){
    let o = document.getElementById("1").getContext("2d")

    let y = 0

    for(let x = 500; x >= 100; x = x - 100){

    o.moveTo(y, y)
    o.lineTo(x, y)

    o.moveTo(x, y)
    o.lineTo(x, x)

    o.moveTo(x, x)
    o.lineTo(y, x)

    o.moveTo(y, x)
    o.lineTo(y, y)

    y = y + 100
    }

    o.stroke()
}