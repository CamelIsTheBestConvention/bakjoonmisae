const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n")[0].split(' ').map(Number);

function parking(num) {
    let sum = 1;
    while (num) {
        sum *= num;
        num--;
    }
    return sum;
}

const [N, A, B, C] = input;
let bestParking = parking(N) / (parking(A) * parking(B) * parking(C));
console.log(bestParking);