#include<stdio.h>
#include<string.h>

int main() {
    int cnt = 1;
    char str[1000001];
    scanf("%[^\n]s", str);

    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == ' ') {
            cnt++;
        }
    }
    // 예제2처럼 문자열 앞에 공백이 발생하면 카운트가 되기 때문에 -1 해줘야한다.
    if (str[0] == ' ' && cnt) {
        cnt--;
    }
    // 위 코드 처럼 뒤에 공백 발생시 -1
    if (str[strlen(str) - 1] == ' ' && cnt) {
        cnt--;
    }

    printf("%d", cnt);

    return 0;
}