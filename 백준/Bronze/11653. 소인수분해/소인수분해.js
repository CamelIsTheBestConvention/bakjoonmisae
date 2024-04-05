const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let n = Number(input[0]);
while(n != 1) {
    for (let i = 2; i <= n; i++) {
        if((n % i) == 0) {    
            n = n / i;
            console.log(i);
            break;
        }
    }
}