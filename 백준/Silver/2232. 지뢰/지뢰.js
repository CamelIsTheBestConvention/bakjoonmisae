const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const mine = (N) => {
    let mineList = [0];
    let mineIndex = []

    for(let i = 1; i <= N; i++) {
        mineList.push(Number(input[i]));
    }
    mineList.push(0);

    for(let i = 1; i <= N; i++) {
        if(mineList[i-1] <= mineList[i] && mineList[i] >= mineList[i+1]) {
            mineIndex.push(i);
        }
    }
    for(let i = 0; i < mineIndex.length; i++) console.log(mineIndex[i]);
}

let N = Number(input[0]);
mine(N);