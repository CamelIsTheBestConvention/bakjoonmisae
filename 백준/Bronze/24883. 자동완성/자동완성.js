const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const word = input[0];

if(word == 'N' || word == 'n') console.log('Naver D2');
else console.log('Naver Whale');