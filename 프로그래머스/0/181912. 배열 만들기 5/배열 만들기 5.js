function solution(intStrs, k, s, l) {
    var answer = [];
    
    for(let i = 0; i < intStrs.length; i++) {
        let a = parseInt(intStrs[i].slice(s, s+l));
        if(a > k) answer.push(a);
    }
    
    return answer;
}