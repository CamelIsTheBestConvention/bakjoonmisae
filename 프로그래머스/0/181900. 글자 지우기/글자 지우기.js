function solution(my_string, indices) {
    var answer = '';
    let arr = my_string.split('');
    let cnt = 0;
    indices.sort((a, b) => a - b);
    
    for (let i = 0; i < arr.length; i++) {
        if(indices[cnt] == i) {
            cnt++;
            continue;
        } else {
            answer += arr[i];
        }

    }
    
    return answer;
}