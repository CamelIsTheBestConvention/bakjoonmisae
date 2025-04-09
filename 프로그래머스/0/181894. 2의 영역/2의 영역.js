function solution(arr) {
    var answer = [];
    const start = arr.indexOf(2);
    const end = arr.lastIndexOf(2);
    
    if(start == -1) {
        answer.push(-1);
        return answer;
    }
    
    for(let i = start; i <= end; i++) {
        answer.push(arr[i]);
    }
    
    return answer;
}