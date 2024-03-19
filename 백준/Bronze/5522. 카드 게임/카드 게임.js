const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let score = 0;

for(let i = 0; i < 5; i++) {
    score += Number(input[i]);
}

console.log(score);