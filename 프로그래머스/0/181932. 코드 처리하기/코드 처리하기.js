function solution(code) {
    var answer = '';
    var mode = 0;
   
    for(let i=0; i<code.length; i++){
       if (mode == 0){
           code[i] == "1" ? (mode = 1 ) : (i % 2 == 0 && (answer += code[i]));
       }else{
           code[i] == "1" ? (mode = 0) : (i % 2 !== 0 && (answer += code[i]));
       }
    }
    
    return answer.length>0 ? answer : "EMPTY";
}