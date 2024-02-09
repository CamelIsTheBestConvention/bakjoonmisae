#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

 // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* rny_string) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int length = strlen(rny_string);
    int m_count = 0;
    
    for (int i = 0; i < length; i++) {
        if(rny_string[i] == 'm'){
            m_count++;
        }
    }

    char* answer = (char*)malloc(sizeof(char) * (length + m_count + 1));
    int j = 0;
    for (int i = 0; i < length; i++) {
        if(rny_string[i] == 'm'){
            answer[j++] = 'r';
            answer[j++] = 'n';
        } else {
            answer[j++] = rny_string[i];
        }
    }
    answer[j] = '\0';

    return answer;
}