const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const Reverse = (secretCode) => {
    let result = '';
    for(let i = secretCode.length; i > 0; i--){
        result += secretCode[i-1];
    }
    console.log(result);
}

let i = 0;
while(true) {
    let code = input[i];
    if(code == 'END') {
        break;
    }
    
    let splitCode = code.split('');
    Reverse(splitCode);
    i++;
}