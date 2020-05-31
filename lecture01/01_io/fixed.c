/* fixed.c: fixed length */

#include <stdio.h>

/* Main execution */

int main(int argc, char *argv[]) {
    int n, x;

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
    	scanf("%d", &x);
    	printf("%d\n", x);
    }

    return 0;
}
