const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let i = 0;

while(true) {    
    let n = Number(input[i]);
    let sum = 0;
    if(n == 0) {
        break;
    }
    for(let j = n; j > 0; j--) {
        sum += j;    
    }
    i++;
    console.log(sum);
}

