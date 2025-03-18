function solution(num_list) {
    var answer = [];
    
    for(let i=0; i<=num_list.length; i++) {
        if(i == num_list.length) {
            if(num_list[i-1] > num_list[i-2]) {
                answer.push(num_list[i-1] - num_list[i-2]);
                break;
            } else {
                answer.push(num_list[i-1]*2);
                break;
            }
        }
        answer.push(num_list[i]);
        
    }
    
    return answer;
}
