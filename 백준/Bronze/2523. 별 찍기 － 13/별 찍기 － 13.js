const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const n = Number(input[0]);
const star = '*';

for (let i = 1; i <= n; i++) {
    let result = '';
    for (let j = 0; j < i; j++) {
        result += star;
    }
    console.log(result);
}
for (let i = n - 1; i > 0; i--) {
    let result = '';
    for (let j = 0; j < i; j++) {
        result += star;
    }
    console.log(result);
}

