const tabs = document.querySelectorAll(".sideBarSection");
const allContents = document.querySelectorAll(".content");

const input = document.getElementById('action')
const par = document.getElementById('par')
const div1 = document.getElementById('mainDiv')
let currentPath = 'D:\Server - Copy Minecraft';

tabs.forEach((tab, index) => {
    tab.addEventListener('click', ()=>{
        tabs.forEach(tab=>{tab.classList.remove('active')})
        tab.classList.add('active')

        allContents.forEach(allContent=>{allContent.classList.remove('tabShow')})
        allContents[index].classList.add('tabShow')
    })
})

let list = [2, 3]

function changeColor(e){
    if(e == 1){
        document.getElementById('1').classList.remove('activeBtn')

        list.forEach((n)=>{
            document.getElementById(`${n}`).classList.add("activeBtn")
        })
    }
    else if(e == 2){
        document.getElementById('1').classList.add('activeBtn')

        list.forEach((n)=>{
            document.getElementById(`${n}`).classList.remove("activeBtn")
        })
    }
}

function run(props) {
    if (props != undefined) {
        let url = '/cgi-bin/main.py?folder=' + props + '&current_path=' + currentPath;
        send(url)
    }
    else {
        let url = '/cgi-bin/main.py';
        send(url)
    }
}

function back(props) {
    let url = '/cgi-bin/main.py?folder=' + props + '&current_path=' + currentPath;
    send(url)
}

function send(url) {
    let oReq = new XMLHttpRequest();

    oReq.onload = runResult;

    oReq.open('GET', url);
    oReq.send();
}

function runResult(e) {

    let result = e.target.response;
    result = JSON.parse(result)
    let title = result[0][0]
    let mainFolder = result[1][0]
    let mainFile = result[2][0]

    let start = 3;
    let end = result.length;

    let subCurrentPathSplit = result.slice(start, end);

    if (currentPath != subCurrentPathSplit.join("")) {
        currentPath = subCurrentPathSplit.join("")
    }

    par.innerHTML = title;
    div1.innerHTML = mainFolder;
    div1.innerHTML += mainFile;

}