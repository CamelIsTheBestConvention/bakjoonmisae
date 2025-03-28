function solution(x1, x2, x3, x4) {
    var answer = true;
    
    if(x1 == true || x2 == true) {
        if(x3 == true || x4 == true) {
            answer = true;
        } else {
            answer = false;
        }
    } else {
        answer = false;
    }
    return answer;
}