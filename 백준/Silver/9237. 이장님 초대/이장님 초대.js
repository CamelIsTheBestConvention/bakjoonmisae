let Invite_EEjang = () => {
    let input = require('fs').readFileSync("/dev/stdin").toString().trim().split('\n');
    const n = Number(input[0]);
    let grow_day = input[1].split(' ').map(Number).sort((a, b) => b - a);
    
    for(let i = 0; i < n; i++) {
        grow_day[i] = grow_day[i] + i + 1;
    }

    console.log(Math.max(...grow_day) + 1);
}

Invite_EEjang();


