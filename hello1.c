#include <stdio.h>

int main(void)
{
    char name[100];  // define an array to store the name
    printf("What's your name? ");
    fgets(name, sizeof(name), stdin);  // read a line of input
    printf("Hello, %s", name);
}
