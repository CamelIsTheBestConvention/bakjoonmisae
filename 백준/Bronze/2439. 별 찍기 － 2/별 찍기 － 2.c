#include <stdio.h>

int main()
{
	int a=0;
	int i;
    int j;
	scanf("%d",&a);

	for(i=1; i<=a; i++)
	{
		for(j=a-i; j>0; j--)
			printf(" ");

		for(j=0; j<i; j++)
			printf("*");

		printf("\n");
	}
	return 0;
}