#include <stdio.h>
#include <string.h>

int main(void)
{
    char answer[10];  // guarda la respuesta del usuario (hasta 9 caracteres + '\0')

    printf("Do you agree? ");
    scanf("%9s", answer);  // lee una palabra

    // Convertir la respuesta a minúsculas manualmente
    for (int i = 0; answer[i]; i++)
    {
        if (answer[i] >= 'A' && answer[i] <= 'Z')
        {
            answer[i] = answer[i] + 32; // convierte de mayúscula a minúscula
        }
    }

    if (strcmp(answer, "y") == 0 || strcmp(answer, "yes") == 0)
    {
        printf("Agreed.\n");
    }
    else if (strcmp(answer, "n") == 0 || strcmp(answer, "no") == 0)
    {
        printf("Not agreed.\n");
    }
    else
    {
        printf("Invalid input.\n");
    }

    return 0;
}
