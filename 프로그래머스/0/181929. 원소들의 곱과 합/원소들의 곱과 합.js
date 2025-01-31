function solution(num_list) {
    var answer = 0;
    let mul = 1;
    let add = 0;
    
    for (let i = 0; i < num_list.length; i++) {
        add += num_list[i];
        mul *= num_list[i];
    }
    
    add *= add;
    
    if (mul < add) {
        answer = 1
    } else {
        answer = 0;
    }
    
    return answer;
}