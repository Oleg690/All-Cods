let moon = document.getElementById('moon');
let text = document.getElementById('text');
let cityLeft = document.getElementById('city-left');
let cityRight = document.getElementById('city-right');

window.addEventListener("scroll",() =>{
    let value = window.scrollY;
    moon.style.top = value * .8 + 'px';
    text.style.marginTop = value * 1.5 + 'px';
    cityLeft.style.left = value * -1.5 + 'px';
    cityRight.style.left = value * 1.5 + 'px';
})