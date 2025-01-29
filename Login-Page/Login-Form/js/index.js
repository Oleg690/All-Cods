const formOpenBtn = document.querySelector('#form-open'),
home = document.querySelector('.home'),
formContainer = document.querySelector('.form_container'),
formCloseBtn = document.querySelector('.form_close'),
singupBtn = document.querySelector('#singup'),
loginBtn = document.querySelector('#login'),
pwShowHide = document.querySelectorAll('.pw_hide');

const body = document.querySelector('.body');

window.addEventListener('scroll', reveal);

function reveal(){
    var reveals = document.querySelectorAll('.reveal');

    for(var i = 0; i < reveals.length; i++){
        var windowheight = window.innerHeight;
        var revealtop = reveals[i].getBoundingClientRect().top;
        var revealpoint = 150;

        if(revealtop < windowheight - revealpoint){
            reveals[i].classList.add('active');
        }
        else{
            reveals[i].classList.remove('active');
        }
    }
}

//------------------------------------------

formOpenBtn.addEventListener("click", () => home.classList.add('show'))
formCloseBtn.addEventListener("click", () => home.classList.remove('show'))

//------------------------------------------

pwShowHide.forEach(icon => {
    icon.addEventListener("click", () => {
        let getPwInput = icon.parentElement.querySelector("input");
        if(getPwInput.type === "password"){
            getPwInput.type = "text"
            icon.classList.replace("uil-eye-slash", "uil-eye")
        }else{
            getPwInput.type = "password"
            icon.classList.replace("uil-eye", "uil-eye-slash")
        }
    })
})

//------------------------------------------

singupBtn.addEventListener('click', (e) => {
    e.preventDefault();
    formContainer.classList.add("active")
})

loginBtn.addEventListener('click', (e) => {
    e.preventDefault();
    formContainer.classList.remove("active")
})

//------------------------------------------