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

// num_list_len은 배열 num_list의 길이입니다.
int solution(int num_list[], size_t num_list_len) {
    int answer = 0;
    int odd;
    int odd_cnt = 0;
    int even;
    int even_cnt = 0;

    for (int i = 0; i < num_list_len; i++) {
        if (num_list[i] % 2 == 1) {
            if (odd_cnt > 0) {
                odd = combine(odd, num_list[i]);
            }
            else {
                odd = num_list[i];
            }
            odd_cnt++;
        }
        else {
            if (even_cnt > 0) {
                even = combine(even, num_list[i]);
            }
            else {
                even = num_list[i];
            }
            even_cnt++;
        }
    }

    answer = odd + even;
    return answer;
}