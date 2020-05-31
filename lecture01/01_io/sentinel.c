/* sentinel.c: sentinel */

#include <stdio.h>

/* Main execution */

int main(int argc, char *argv[]) {
    int n;

    while (scanf("%d", &n) && n > 0) {
    	printf("%d\n", n);
    }
    return 0;
}
