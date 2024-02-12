#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int combine(int a, int b) {
    int first = a;
    int second = b;
    while (second > 0) {
        first *= 10;
        second /= 10;
    }

    return first + b;
}

int solution(int a, int b) {
    int answer = 0;
    int first;
    int second;
    first = 2*a*b;
    second = combine(a, b);
    
    if(first > second) {
        answer = first;
    } else {
        answer = second;
    }
    
    return answer;
}