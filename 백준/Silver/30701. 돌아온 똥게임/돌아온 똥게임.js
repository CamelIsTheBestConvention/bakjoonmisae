const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
let [N, D] = input[0].split(" ").map(Number);
let kunhoPower = D;
let battleRoom = [];
let weaponRoom = [];
let clearRoom;

for(let i = 1; i <= N; i++) {
    let [type, x] = input[i].split(" ").map(Number);
    if(type == 1) {
        battleRoom.push(x);
    } else {
        weaponRoom.push(x);
    }
}

battleRoom.sort((a, b) => a - b);
weaponRoom.sort((a, b) => a - b);

clearRoom = weaponRoom.length;
while (battleRoom.length > 0) {
    while (weaponRoom.length > 0 && kunhoPower <= battleRoom[0]) {
        kunhoPower *= weaponRoom.shift();
    }
    if (kunhoPower > battleRoom[0]) {
        clearRoom++;
        kunhoPower += battleRoom.shift();
    }
    else break;
}
console.log(clearRoom);