const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const TheGameOfDeath = (N, K) => {
    const order = [];
    for(let i = 1; i <= N; i++) {
        order.push(Number(input[i].replace(/\r/g, '')));
    }

    let death = 0;
    let count = 0;
    let visited = Array(N).fill(0);

    while(true) {
        if(death === K) {
            console.log(count);
            break;
        }
        if(visited[death]) {
            console.log(-1);
            break;
        }
        visited[death] = 1;
        death = order[death];
        count++;
    }
}

const [N, K] = input[0].split(" ").map(Number);

TheGameOfDeath(N, K);