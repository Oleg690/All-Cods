let counter = 0


document.getElementById('resetBtn').onclick = function(){
    counter = 0
    document.getElementById('countLabel').innerHTML = 0
}
document.getElementById('decreaseBtn').onclick = function(){
    counter -= 1
    document.getElementById('countLabel').innerHTML = counter
}
document.getElementById('increaseBtn').onclick = function(){
    counter += 1
    document.getElementById('countLabel').innerHTML = counter
}