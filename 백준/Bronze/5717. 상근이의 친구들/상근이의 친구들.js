const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let i = 0;

while(true) {
    let [n, m] = input[i].split(' ').map(Number);
    if(n == 0 && m == 0) break;
    console.log(n + m);
    i++
}