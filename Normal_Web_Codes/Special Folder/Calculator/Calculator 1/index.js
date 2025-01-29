const display = document.querySelector('#display');
const buttons = document.querySelectorAll('button');
const btn_operators = document.getElementsByClassName('btn-operator');

let lastButtonIsOperator = false;

buttons.forEach((item) => {
    item.onclick = () => {
        if (item.classList.contains('btn-operator')) {
            if (lastButtonIsOperator) {
                return; // Don't allow consecutive operator buttons
            }
            lastButtonIsOperator = true;
        } else {
            lastButtonIsOperator = false;
        }

        if (item.id == 'clear'){
            display.innerText = '';
        } else if (item.id == 'backspace'){
            let string = display.innerText.toString();
            display.innerText = string.substr(0, string.length - 1);
        } else if (display.innerText != '' && item.id == 'equal'){
            display.innerText = eval(display.innerText);
        } else if (display.innerText == '' && item.id == 'equal'){
            display.innerText = 'Empty!';
            setTimeout(() => (display.innerText = ''), 2000);
        } else {
            if (item.classList.contains('btn-number')) {
                if (display.innerText === '0') {
                    display.innerText = ''; // Remove leading zero
                }
            }
            display.innerText += item.id;
        }
    } 
});

const themeToggBtn = document.querySelector('.theme-toggler');
const calculator = document.querySelector('.calculator');
const toggleIcon = document.querySelector('.toggler-icon');
let isDark = true;

themeToggBtn.onclick = () => {
    calculator.classList.toggle('dark');
    themeToggBtn.classList.toggle('active');
    isDark = !isDark;
};