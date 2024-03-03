const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const itemMaster = (N) => {
    const studentScore = [];
    const item_master = [];

    for(let i = 1; i <= N; i++) {
        let score = input[i].split(" ").map(Number);
        studentScore.push(score);
    }

    for(let j = 1; j <= 4; j++) {
        studentScore.sort((a, b) => {
            if (b[j] !== a[j]) {
                return b[j] - a[j];
            } else {
                return a[0] - b[0];
            }
        });

        for(let k = 0; k < N; k++) {
            if (!item_master.includes(studentScore[k][0])) {
                item_master.push(studentScore[k][0]);
                break;
            }
        }
    }

    console.log(item_master.join(' '));
}

let N = Number(input[0]);

itemMaster(N);
