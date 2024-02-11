#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h> 

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* str1, const char* str2) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int str1length = strlen(str1);
    int str2length = strlen(str2);
    int total_length = str1length + str2length;
    char* answer = (char*)malloc((sizeof(char)*total_length)+1);
    int cnt = 0;

    for (int i = 0; i < total_length; i+=2) {
            answer[i] = str1[cnt];
            answer[i+1] = str2[cnt];
            cnt++;
    }
    
    answer[total_length] = '\0';

    return answer;
}