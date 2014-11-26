/*
    [Recusion] Print a string in reverse order.
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void printReverse(const char *str)
{
    if(*str)
    {
        printReverse(str + 1);
        putchar(*str);
    }
}

int main(int argc, const char* argv[])
{
    printReverse("abcdefg");
}