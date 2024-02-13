#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

combine(int a, int b) {
    int first = a;
    int second = b;
    while(second > 0) {
        first *= 10;
        second /= 10;
    }
    
    return first + b;
}

int solution(int a, int b) {
    int answer = 0;
    int temp1 = 0;
    int temp2 = 0;
    temp1 = combine(a, b);
    temp2 = combine(b, a);
    if(temp1>temp2) {
        answer = temp1;
    } else {
        answer = temp2;
    }
    return answer;
}