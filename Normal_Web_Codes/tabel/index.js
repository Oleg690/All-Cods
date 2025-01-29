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





    canvas.moveTo(0, 50)
    canvas.lineTo(500, 50)

    canvas.moveTo(0, 100)
    canvas.lineTo(500, 100)

    canvas.moveTo(0, 150)
    canvas.lineTo(500, 150)

    canvas.moveTo(0, 200)
    canvas.lineTo(500, 200)

    canvas.moveTo(0, 250)
    canvas.lineTo(500, 250)

    canvas.moveTo(0, 300)
    canvas.lineTo(500, 300)

    canvas.moveTo(0, 350)
    canvas.lineTo(500, 350)

    canvas.moveTo(0, 400)
    canvas.lineTo(500, 400)

    canvas.moveTo(0, 450)
    canvas.lineTo(500, 450)

    for(let x = 50; x <= 450; x = x + 50){
        canvas.moveTo(x, 0)
        canvas.lineTo(x, y)
    }

    canvas.stroke()
}