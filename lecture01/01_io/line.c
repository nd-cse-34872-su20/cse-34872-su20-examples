/* line.c: line-oriented */

#include <stdio.h>

/* Main execution */

int main(int argc, char *argv[]) {
    char buffer[BUFSIZ];

    while (fgets(buffer, BUFSIZ, stdin)) {
    	int x, y;
    	sscanf(buffer, "%d %d", &x, &y);
    	printf("%d %d\n", x, y);
    }

    return 0;
}
