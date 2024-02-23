let Dungchi = () => {
    const fs = require("fs");
    const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
    let input = fs.readFileSync(filePath).toString().split("\n");

    const n = Number(input[0]);
    let people = [];

    for(let i = 1; i <= n; i++) {
        const [weight, height] = input[i].split(" ").map(Number);
        people.push({weight, height});
    }

    for(let i = 0; i < n; i++) {
        let rank = 1;
        for(let j = 0; j < n; j++) {
            if(i !== j && people[i].weight < people[j].weight && people[i].height < people[j].height) {
                rank++;
            }
        }
        process.stdout.write(rank + " ");
    }
}

Dungchi()