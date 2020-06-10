/* subsets.c */

#include <stdio.h>

/* Functions */

int divisible_subsets(int n) {
    /* TODO: Use bitsets to count number of subsets divisible by n */
}

/* Main execution */

int main(int argc, char *argv[]) {
    int n;

    while (scanf("%d", &n) != EOF) {
    	printf("%d\n", divisible_subsets(n));
    }

    return 0;
}
