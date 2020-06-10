/* subsets.c */

#include <stdio.h>

/* Functions */

int divisible_subsets(int n) {
    int count = 0;

    for (int bitset = 0; bitset < (1<<10); bitset++) {
    	int total = 0;
    	for (int i = 0; i < 10; i++) {
    	    total += (bitset & (1<<i)) ? i : 0;
	}
	count += (total % n == 0);
    }

    return count;
}

/* Main execution */

int main(int argc, char *argv[]) {
    int n;

    while (scanf("%d", &n) != EOF) {
    	printf("%d\n", divisible_subsets(n));
    }

    return 0;
}
