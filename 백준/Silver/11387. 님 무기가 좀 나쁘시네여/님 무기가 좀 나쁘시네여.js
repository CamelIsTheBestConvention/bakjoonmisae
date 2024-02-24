const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const power = (h, w) => {
    return (h[0]+w[0]) * (100+h[1]+w[1]) * (100 * (100-Math.min(h[2]+w[2], 100)) + Math.min(h[2]+w[2], 100) * (h[3]+w[3])) * (100+h[4]+w[4]);
}

const input = [];
rl.on('line', (line) => {
    input.push(line.split(' ').map(Number));
}).on('close', () => {
    const h1 = input[0];
    const h2 = input[1];
    const w1 = input[2];
    const w2 = input[3];

    for(let i =0; i < 5; i++) {
        h1[i] -= w1[i];
        h2[i] -= w2[i];
    }

    const diff1 = power(h1, w2) - power(h1, w1);
    const diff2 = power(h2, w1) - power(h2, w2);

    console.log(diff1 > 0 ? '+' : diff1 === 0 ? '0' : '-');
    console.log(diff2 > 0 ? '+' : diff2 === 0 ? '0' : '-');

    process.exit();
});
