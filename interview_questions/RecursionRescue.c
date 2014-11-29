/*
    Given only putchar (no sprintf, itoa, etc.) write a routine putlong that
    prints out an unsigned long in decimal.
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void putlong(unsigned long l)
{
    if (l < 10)
    {
        putchar(48 + l);
        return;
    }
    unsigned long u = l % 10;
    putlong(l / 10);
    putchar(48 + u);
}

int main(int argc, const char* argv[])
{
    long a = 123;
    printf("a: %ld \n", a);

    long b = -123;
    printf("b: %ld \n", b);


    unsigned long x = 123;
    printf("x: %lu \n", x);

    unsigned long y = -123;
    printf("y: %lu \n", y);

    unsigned long z = 0;
    printf("z: %lu \n", z);

    printf("?: %d \n", 0 / 10);

    unsigned long l = 123;
    putlong(l);
    printf("\n");

    l = -123;
    putlong(l);
    printf("\n");

    l = 1023;
    putlong(l);
    printf("\n");

    l = 10;
    putlong(l);
    printf("\n");

    l = 7;
    putlong(l);
    printf("\n");

    l = 0;
    putlong(l);
    printf("\n");
}