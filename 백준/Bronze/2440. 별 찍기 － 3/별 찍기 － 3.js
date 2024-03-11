const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const n = Number(input[0]);
const star = '*';

for (let i = 0; i < n; i++) {
    let result = '';
    for (let j = n; j > i; j--) {
        result += star;
    }
    console.log(result);
}

