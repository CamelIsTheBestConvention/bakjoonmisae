function solution(n) {
    var answer = [];
    let a = n;
    answer.push(n);
    
    while(true) {
        if(a == 1) break;
        
        if (a % 2 == 0) {
            a /= 2;
            answer.push(a);
        } else {
            a = 3*a+1;
            answer.push(a);
        }
    }
    
    return answer;
}