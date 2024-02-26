const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

// N:운동시간, m=초기맥박, M=한계맥박, T=증가맥박, R=감소맥박
//      5           70         120         25           15
let [N, m, M, T, R] = input[0].split(" ").map(Number);
let exercise = 0;
let totalExercise = 0;
let curPulse = m;

while(exercise !== N)
{
    totalExercise++;

    if(m+T <= M)
    {
        m += T;
        exercise++;
    }
    else
    {
        m -= R;

        if(m < curPulse) m = curPulse;
    }

    if((m + T > M) && (m == curPulse)) break;
}

if(exercise !== N) console.log(-1);
else console.log(totalExercise);