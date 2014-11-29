#include <stdio.h>

void function1(int *pt)
{
    printf("function1: %d\n", *pt);
}

void function2(int **pt)
{
    printf("function2: %d\n", **pt);
}

int main(int argc, const char* argv[])
{
    int val = 10;
    int* pt1 = &val;
    int** pt2 = &pt1;

    printf("1: %d\n", val);
    printf("2: %d\n", *pt1);
    printf("3: %d\n", **pt2);

    function1(pt1);
    function2(pt2);

}