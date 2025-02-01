const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    let arr = str.split('');
    let result = '';
    
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] === arr[i].toUpperCase()) {
            result += arr[i].toLowerCase();
        } else {
            result += arr[i].toUpperCase();
        }
    }
    
    console.log(result);
});