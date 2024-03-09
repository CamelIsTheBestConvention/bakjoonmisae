const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const n = input[0];

if (n == 0) console.log('YONSEI');
else console.log('Leading the Way to the Future');