const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let jaehwan_voice = input[0];
let doctor_voice = input[1];

if(jaehwan_voice.length >= doctor_voice.length) console.log('go');
else console.log('no');
