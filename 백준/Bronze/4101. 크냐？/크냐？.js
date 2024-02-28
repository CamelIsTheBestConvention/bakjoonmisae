const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

i = 0;
while(input[i]){
    const [num1, num2] = input[i].split(" ").map(Number);
    if(num1 == 0 && num2 == 0) {
        break;
    }
    if(num1 > num2) console.log("Yes");
    else console.log("No");
    i++;
}