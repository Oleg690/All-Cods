function run(){
    let x = document.getElementById("1").getContext("2d")

    x.moveTo(0, 0)
    x.lineTo(100, 0)

    x.moveTo(100, 0)
    x.lineTo(100, 100)

    x.moveTo(100, 100)
    x.lineTo(200, 100)

    x.moveTo(200, 100)
    x.lineTo(200, 200)

    x.moveTo(200, 200)
    x.lineTo(300, 200)

    x.moveTo(300, 200)
    x.lineTo(300, 300)

    x.moveTo(300, 300)
    x.lineTo(400, 300)

    x.moveTo(400, 300)
    x.lineTo(400, 400)

    x.moveTo(400, 400)
    x.lineTo(500, 400)

    x.moveTo(500, 400)
    x.lineTo(500, 500)


    x.stroke()
}