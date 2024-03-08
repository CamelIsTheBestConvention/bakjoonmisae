const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const Airpot = (n) => {
    const phoneList = input[1].split(" ").map(Number);
    let batteryUse = 0;
    let lastPhone = -1;
    let lastPhoneUse = -1;

    for(let i = 0; i < n; i++) {
        if(phoneList[i] == lastPhone) { 
            batteryUse += lastPhoneUse*2; 
            lastPhoneUse *= 2;
        } else {
            batteryUse += 2; 
            lastPhoneUse = 2;
        }
        lastPhone = phoneList[i];
        
        if(batteryUse >= 100) {
            batteryUse = 0;
            lastPhone = -1;
            lastPhoneUse = -1;
        }
    }
    console.log(batteryUse);
}

const n = Number(input[0]);
Airpot(n);
