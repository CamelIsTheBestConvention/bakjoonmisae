function solution(n, control) {
    var answer = n;
    let arr = control.split('');
    
    for (let i = 0; i < arr.length; i++) {
        switch(arr[i]) {
            case 'w':
                answer += 1;
                continue;
            case 's':
                answer -= 1;
                continue;
            case 'd':
                answer += 10;
                continue;
            case 'a':
                answer -= 10;
                continue;
        }
    }
    
    
    return answer;
}