function run(){
    let canvas = document.getElementById("1").getContext("2d")

    let y = 500

    canvas.moveTo(0, 0)
    canvas.lineTo(500, 0)

    canvas.moveTo(0, 0)
    canvas.lineTo(0, 500)

    canvas.moveTo(0, 500)
    canvas.lineTo(500, 500)

    canvas.moveTo(500, 500)
    canvas.lineTo(500, 0)





    canvas.moveTo(0, 100)
    canvas.lineTo(500, 100)

    canvas.moveTo(0, 200)
    canvas.lineTo(500, 200)

    canvas.moveTo(0, 300)
    canvas.lineTo(500, 300)

    canvas.moveTo(0, 400)
    canvas.lineTo(500, 400)

    canvas.moveTo(0, 500)
    canvas.lineTo(500, 500)

    for(let x = 100; x <= 500; x = x + 100){
        canvas.moveTo(x, 0)
        canvas.lineTo(x, y)
    }

    canvas.stroke()
}