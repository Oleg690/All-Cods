info = document.getElementById('info');
resultTextName = document.getElementById('resultName');
resultTextAge = document.getElementById('resultAge');

let nameInfo = ''
let age = ''

function run(){
    x = info.value;
    infoAll = x.split(' ');
    getAge();
    getName();
    resultTextName.innerHTML = nameInfo + ':' + age;
}

function getAge(){
    nameInfo = infoAll[0]
}

function getName(){
    age = infoAll[1]
}