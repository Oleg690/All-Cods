let a
let b
let c

a = document.getElementById("aText")
a = Number(a)
console.log(a)
b = document.getElementById('bText')
b = Number(b)
c = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2))

document.getElementById('Button').onclick = function(){
    a = document.getElementById("aText").value
    a = Number(a)
    b = document.getElementById('bText').value
    b = Number(b)
    c = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2))
    document.getElementById('cLabel').innerHTML = 'Side C is: ' + c
}