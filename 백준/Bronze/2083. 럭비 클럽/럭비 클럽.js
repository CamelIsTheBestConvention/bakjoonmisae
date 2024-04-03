const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let i = 0;
while(true) {
    const [name, age, weight] = input[i].split(' ').map(item => {
        return isNaN(item) ? item : parseInt(item, 10);
    });
    if(name == '#' && age == 0 && weight == 0) {
        break;
    }
    if(age > 17 || weight >= 80) {
        console.log(name + ' Senior');
    } else {
        console.log(name + ' Junior');
    }
    i++;
}
