#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main(void) {
	int n;
	scanf("%d", &n);

	printf("int a;\n");
	if (n == 1) {
		printf("int *ptr = &a;\n");
	}
	else if (n == 2) {
		printf("int *ptr = &a;\n");
		printf("int **ptr2 = &ptr;\n");
	}
	else {
		printf("int *ptr = &a;\n");
		printf("int **ptr2 = &ptr;\n");
		for (int i = 3; i < n+1; i++) {
			printf("int ");
			for (int j = 0; j < i; j++) {
				printf("*");
			}
			printf("ptr%d = &ptr%d;\n", (i), (i - 1));
		}
	}

	return 0;
}