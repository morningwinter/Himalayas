#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

void countWords(char *str)
{
    int wordCount = 0;
    bool wordStarted = false;
    char *p1 = str;
    while(*p1)
    {
        if(wordStarted && *p1 == ' ')
        {
            wordStarted = false;
        }
        else if(wordStarted == false)
        {
            wordCount++;
            wordStarted = true;
        }
        p1++;
    }
    printf("%d", wordCount);
}

int main(int argc, const char* argv[])
{
    countWords("Hello, my name is John.");
}