#include <stdio.h>

int main() {
    int i, n, num, max = 0;
    float sum = 0;
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        scanf("%d", &num);
        sum += num;
        if (num > max) max = num;
    }
    printf("%f", ((sum / max) * 100) / n);
    return 0;
}