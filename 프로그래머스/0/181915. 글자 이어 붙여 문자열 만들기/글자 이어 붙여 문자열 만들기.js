function solution(my_string, index_list) {
    var answer = '';
    let wordList = my_string.split('');
    
    for (let i = 0; i < index_list.length; i++) {
        answer += wordList[index_list[i]];
    }
    
    return answer;
}