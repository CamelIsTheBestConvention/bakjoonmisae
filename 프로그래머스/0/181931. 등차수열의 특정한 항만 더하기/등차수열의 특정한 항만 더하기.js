function solution(a, d, included) {
    var answer = 0;
    let sum = a;
    
    for (let i = 0; i < included.length; i++) {

        if (included[i] == true) {
            answer += sum;
            sum += d;
        } else {
            sum += d;
            continue;
        }
    }
    return answer;
}