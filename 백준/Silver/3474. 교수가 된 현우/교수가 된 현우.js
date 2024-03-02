const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

T = Number(input[0]);

for(let i = 1; i <= T; i++) {
    let num = input[i];
    let count = 0;
    
    while(num >= 5) {
        count += Math.floor(num / 5);
        num /= 5;
    }
    console.log(count);
}