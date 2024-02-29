let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let [N, D] = input[0].split(" ").map(Number);
let monster = [];
let item = [];

for(let i = 1; i <= N; i++) {
    let [type, x] = input[i].split(" ").map(Number);
    if(type == 1) {
        monster.push(x);
    } else {
        item.push(x);
    }
}

monster.sort((a, b) => a - b);
item.sort((a, b) => a - b);

let ans = item.length; //아이템 방은 무조건 돌파 가능
while (monster.length > 0) {
    while (item.length > 0 && monster[0] >= D) { //장비가 남아있고 아직 몬스터를 쓰러트릴 수 없다면
        D *= item.shift();
    }
    if (monster[0] < D) { //쓰러트릴 수 있다면
        ans++;
        D += monster.shift();
    }
    else break; //불가능
}
console.log(ans);
