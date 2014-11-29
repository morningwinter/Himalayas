#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void removeSpaces(char *str)
{
    int length = strlen(str);
    char *p1 = str;
    char *p2 = malloc(length + 1);
    char *p3 = p2;

    int j = 0;
    while (1)
    {
        
        while (*p1 == ' ')
        {
            p1++;
        }

        if (*p1 == '\0')
        {
            *p2 = *p1;
            break;
        }

        *p2++ = *p1++;
        //p1++;
        //p2++;
    }

    printf("x: %s \n", p3);
}

int main(int argc, const char* argv[])
{
    removeSpaces("abc de");
}