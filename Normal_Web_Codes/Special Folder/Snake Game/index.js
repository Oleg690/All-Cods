const playBoard = document.querySelector('.play-board');
const scoreElement = document.querySelector('.score');
const hightScoreElement = document.querySelector('.hight-score');
const controsls = document.querySelectorAll('.controls i');

let gameOver = false;
let foodX, foodY;
let SnakeX = 5, snakeY = 5;
let velocityX = 0, velocityY = 0;
let snakeBody = [];
let setIntervalId;
let score = 0;

