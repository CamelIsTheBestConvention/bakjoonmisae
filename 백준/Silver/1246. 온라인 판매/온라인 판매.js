let OnlineSell = () => {
    const fs = require("fs");
    const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
    let input = fs.readFileSync(filePath).toString().split("\n");

    const [n, m] = input[0].split(" ").map(Number);
    const prices = input.slice(1, m+1).map(Number).sort((a, b) => b - a);
    
    let margin = 0;
    let priceegg = 0;

    for (let i = 0; i < prices.length; i++) {
        let lowprice = prices[i] * Math.min(n, i+1);
        if (lowprice > margin) {
            margin = lowprice;
            priceegg = prices[i];
        }
    }

    console.log(priceegg + " " + margin);
}

OnlineSell();
