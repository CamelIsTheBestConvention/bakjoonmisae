#include <stdio.h>

int stack[1000000];
int top = -1;

void push(int x) {
	stack[++top] = x;
}

int pop() {
	if(top == -1) 
		return -1;
	else
		return stack[top--];
}

int size() {
	return top + 1;
}

int empty() {
	if (top == -1) return 1;
	else return 0;
}

int checkstack() {
	if (top == -1) return -1;
	else return stack[top];
}

int main() {
	int n;
	int x;
	int order;

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &order);

		switch (order) {
			case 1:
				scanf("%d", &x);
				push(x);
				break;
			case 2:
				printf("%d\n", pop());
				break;
			case 3:
				printf("%d\n", size());
				break;
			case 4:
				printf("%d\n", empty());
				break;
			case 5:
				printf("%d\n", checkstack());
				break;
		}
	}
	return 0;
}