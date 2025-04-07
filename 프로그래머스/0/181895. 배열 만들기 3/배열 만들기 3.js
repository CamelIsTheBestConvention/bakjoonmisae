function solution(arr, intervals) {
    var answer = [];
    
    for(let i = 0; i < intervals.length; i++) {
        const [start, end] = intervals[i];
        
        for (let j = start; j <= end; j++) {
            answer.push(arr[j]);
        }
    }
    
    return answer;
}