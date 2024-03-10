const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const yourHandle = (n, i) => {
    const handle = [];
    for(let i = 1; i <= n; i++) {
        handle.push(input[i].replace(/\r/g, ''));
    }

    handle.sort();

    console.log(handle[i-1]);
}

const [n, i] = input[0].split(' ').map(Number);

yourHandle(n, i);